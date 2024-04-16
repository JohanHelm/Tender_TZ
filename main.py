from requests import Session

from get_parse import GetPageData, parse_xml_form, parse_main_page


headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}


def main():
    main_urls = ("https://zakupki.gov.ru/epz/order/extendedsearch/results.html?fz44=on&pageNumber=1",
                 "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?fz44=on&pageNumber=2")
    session = Session()
    session.headers.update(headers)
    gpd = GetPageData()
    for url in main_urls:
        html_response = gpd.run(url, session)
        for xml_link in parse_main_page(html_response):
            xml_response = gpd.run(xml_link, session)
            print(xml_link, parse_xml_form(xml_response))


if __name__ == "__main__":
    main()
