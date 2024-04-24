from get_parse import GetPageData, GetXmlForm
from re import fullmatch


def test_main_page(create_session):
    gpd = GetPageData(create_session)
    pattern = "https:\/\/zakupki.gov.ru\/epz\/order\/notice\/printForm\/viewXml\.html\?regNumber=[0-9]{19}"
    assert all([fullmatch(pattern, link) for link in
                gpd.run("https://zakupki.gov.ru/epz/order/extendedsearch/results.html?fz44=on&pageNumber=1")])

def test_xml_form(create_session):
    gxf = GetXmlForm(create_session)
    assert gxf.run("https://zakupki.gov.ru/epz/order/notice/printForm/viewXml.html?regNumber=0338300019624000023") == \
           "2024-04-03T15:37:43.491+12:00"
