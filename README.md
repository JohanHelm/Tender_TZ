# Tender_TZ
Задача
1. Спарсить ссылки на xml с первых двух страниц сайта https://zakupki.gov.ru/epz/order/extendedsearch/results.html
2. Перейти по ссылкам и распарсить XML, вынуть артибут publishDTInEIS

Для запуска
1. создать венв, установить зависимости
2. запустить венв
3. запустить селери командой python -m celery -A get_parse worker --loglevel=info
4. Запустить сервер редис. Если приходит ошибка, тогда: redis-cli; SHUTDOWN
5. для запуска приложения python main.py
6. для запуска тестов python -m pytest test_get_parse.py