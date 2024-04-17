from requests import Session

from get_parse import GetPageData, GetXmlForm


headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}


def main():
    main_urls = ("https://zakupki.gov.ru/epz/order/extendedsearch/results.html?fz44=on&pageNumber=1",
                 "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?fz44=on&pageNumber=2")
    session = Session()
    session.headers.update(headers)
    gpd = GetPageData(session)
    gxf = GetXmlForm(session)
    for url in main_urls:
        print_link_iterator = gpd.run(url)
        for xml_link in print_link_iterator:
            result = gxf.run(xml_link)
            print(xml_link, result)


if __name__ == "__main__":
    main()
