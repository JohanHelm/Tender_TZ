from requests import Session
from requests.models import Response
from bs4 import BeautifulSoup
from celery import Celery, Task
from typing import Iterator


app = Celery("get_parse", backend="redis://localhost:6379",  broker="redis://localhost:6379")


class GetPageData(Task):
    def run(self, link: str, session: Session) -> Response:
        return session.get(link, timeout=3)


def parse_main_page(response: Response) -> Iterator[str]:
    html_soup = BeautifulSoup(response.text, "lxml")
    print_blocks_list = html_soup.find_all("div",
                                           attrs={"class": "w-space-nowrap ml-auto registry-entry__header-top__icon"})
    for print_block in print_blocks_list:
        print_link_block = print_block.find("a", attrs={"target": "_blank"})
        part_print_link = print_link_block.get("href").replace("view.html", "viewXml.html")
        print_link_xml = f"https://zakupki.gov.ru{part_print_link}"
        yield print_link_xml


def parse_xml_form(response: Response) -> str | None:
    soup = BeautifulSoup(response.text, features="xml")
    result = soup.find("publishDTInEIS")
    if result:
        return result.text
    return result


class GetHelloWorld(Task):
    def run(self):
        return ["hello world"]
