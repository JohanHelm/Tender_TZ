# Tender_TZ
Задача
1. Спарсить ссылки на xml с первых двух страниц сайта https://zakupki.gov.ru/epz/order/extendedsearch/results.html
2. Перейти по ссылкам и распарсить XML, вынуть артибут publishDTInEIS.

Для запуска
1. Cоздать венв, установить зависимости.
2. Запустить венв.
3. Запустить селери командой python -m celery -A get_parse worker --loglevel=info.
4. Запустить сервер редис. Если приходит ошибка, тогда: redis-cli && SHUTDOWN.
5. Для запуска приложения python main.py.
6. Для запуска тестов python -m pytest test_get_parse.py.