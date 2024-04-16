from aiohttp.client import ClientSession
from bs4 import BeautifulSoup
from celery import Celery, Task

app = Celery("get_parse", backend="redis://localhost:6379",  broker="redis://localhost:6379")


headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}


async def get_main_page_data(link: str):
    async with ClientSession() as session:
        async with session.get(link, headers=headers, timeout=3) as response:
            html_soup = BeautifulSoup(await response.text(), "lxml")
            return html_soup


async def parse_main_page(html_soup) -> list[str, ...]:
    print_link_xml_list = []
    print_blocks_list = html_soup.find_all("div",
                                           attrs={"class": "w-space-nowrap ml-auto registry-entry__header-top__icon"})
    for print_block in print_blocks_list:
        print_link_block = print_block.find("a", attrs={"target": "_blank"})
        part_print_link = print_link_block.get("href").replace("view.html", "viewXml.html")
        print_link_xml = f"https://zakupki.gov.ru{part_print_link}"
        print_link_xml_list.append(print_link_xml)
    return print_link_xml_list


@app.task
async def get_parse_xml_form(link: str) -> str | None:
    async with ClientSession() as session:
        async with session.get(link, headers=headers, timeout=3) as response:
            soup = BeautifulSoup(await response.text(), features="xml")
            result = soup.find("publishDTInEIS")
            if result:
                return result.text
            return result


@app.task
def get_hello_world():
    return "hello world"


main_urls = ("https://zakupki.gov.ru/epz/order/extendedsearch/results.html?fz44=on&pageNumber=1",
             "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?fz44=on&pageNumber=2")
# asyncio.run(get_html_data(main_urls[0]))
