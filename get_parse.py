from requests.models import Response
from bs4 import BeautifulSoup
from celery import Celery, Task
from typing import Iterator


app = Celery("get_parse", backend="redis://localhost:6379",  broker="redis://localhost:6379")


class GetPageData(Task):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def run(self, link: str) -> Iterator[str]:
        response: Response = self.session.get(link, timeout=3)
        html_soup = BeautifulSoup(response.text, "lxml")
        print_blocks_list = html_soup.find_all("div",
                                               attrs={"class": "w-space-nowrap ml-auto registry-entry__header-top__icon"})
        for print_block in print_blocks_list:
            print_link_block = print_block.find("a", attrs={"target": "_blank"})
            part_print_link = print_link_block.get("href").replace("view.html", "viewXml.html")
            print_link_xml = f"https://zakupki.gov.ru{part_print_link}"
            yield print_link_xml


class GetXmlForm(Task):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def run(self, link: str) -> str | None:
        response: Response = self.session.get(link, timeout=3)
        soup = BeautifulSoup(response.text, features="xml")
        result = soup.find("publishDTInEIS")
        if result:
            return result.text
        return result


class CoiZhiv(Task):
    def run(self):
        return "Цой жив!!!"
