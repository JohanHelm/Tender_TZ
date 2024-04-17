from get_parse import GetPageData, GetXmlForm


def test_main_page(create_session):
    gpd = GetPageData(create_session)
    assert tuple(gpd.run("https://zakupki.gov.ru/epz/order/extendedsearch/results.html?fz44=on&pageNumber=1")) == \
           ("https://zakupki.gov.ru/epz/order/notice/printForm/viewXml.html?regNumber=0338300019624000023",
            "https://zakupki.gov.ru/epz/order/notice/printForm/viewXml.html?regNumber=0138100003124000021",
            "https://zakupki.gov.ru/epz/order/notice/printForm/viewXml.html?regNumber=0138300000124000077",
            "https://zakupki.gov.ru/epz/order/notice/printForm/viewXml.html?regNumber=0138100003124000022",
            "https://zakupki.gov.ru/epz/order/notice/printForm/viewXml.html?regNumber=0338200009824000180",
            "https://zakupki.gov.ru/epz/order/notice/printForm/viewXml.html?regNumber=0338200009824000210",
            "https://zakupki.gov.ru/epz/order/notice/printForm/viewXml.html?regNumber=0888500000224000139",
            "https://zakupki.gov.ru/epz/order/notice/printForm/viewXml.html?regNumber=0338200013924000114",
            "https://zakupki.gov.ru/epz/order/notice/printForm/viewXml.html?regNumber=0188300000224000034",
            "https://zakupki.gov.ru/epz/order/notice/printForm/viewXml.html?regNumber=0338200010024000036")

def test_xml_form(create_session):
    gxf = GetXmlForm(create_session)
    assert gxf.run("https://zakupki.gov.ru/epz/order/notice/printForm/viewXml.html?regNumber=0338300019624000023") == \
           "2024-04-03T15:37:43.491+12:00"
