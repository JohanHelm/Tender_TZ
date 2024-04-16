from get_parse import get_main_page_data, get_parse_xml_form, parse_main_page, get_hello_world


main_urls = ("https://zakupki.gov.ru/epz/order/extendedsearch/results.html?fz44=on&pageNumber=1",
             "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?fz44=on&pageNumber=2")


def main():
    result = get_hello_world.delay()
    print(result.get())


if __name__ == "__main__":
    main()

