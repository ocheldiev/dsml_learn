Создание тестовой базы данных.

Для создания тестовой базы данных необходимо выполнить файл shop_db_create.py. 
Пример запуска:
py shop_db_create.py
или
python3 shop_db_create.py
Скрипт создаст файл shop.db с базой данных sqlite в текущей директории скрипта и наполнит его тестовыми данными

Запуск сервиса.

Для запуска сервиса необходимо выполнить файл homework1.py
Пример запуска:
py homework1.py
или
python3 homework1.py

Описание методов

Метод POST /post_sales
Обрабатывает POST-запрос с json-телом для сохранения данных о произведенной продаже (id товара + id магазина)
При запуске локально endpoint http://127.0.0.1:8080/post_sales
Пример вызова метода на python
import http.client
import json
conn = http.client.HTTPSConnection("127.0.0.1", 8080)
payload = json.dumps({
  "item_id": 10,
  "store_id": 3
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/post_sales", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

Передаются данные в формате json

{
  "item_id": идентификатор товара,
  "store_id": магазин где продан товар
}

Метод GET /get_stores
Обрабатывает GET-запрос на получение всех магазинов
При запуске локально endpoint http://127.0.0.1:8080/get_stores
Формат выходных данных json
Пример ответа:
{
    "stores": [
        {
            "store_id": 1,
            "address": "Москва"
        },
        {
            "store_id": 2,
            "address": "Питер"
        }
    ]
}

store_id - идентификатор магазина для метода POST /post_sales
address - адрес магазина 

Метод GET /get_items
Обрабатывает GET-запрос на получение всех товарных позиций
При запуске локально endpoint http://127.0.0.1:8080/get_items
Формат выходных данных json
Пример ответа:
{
    "items": [
        {
            "item_id": 1,
            "name": "Товар1",
            "price": 10.0
        },
        {
            "item_id": 2,
            "name": "Товар2",
            "price": 20.0
        }
    ]
}

item_id - идентификатор товара для метода POST /post_sales
name - нименование товара
price - цена товара

Метод GET /get_top_stores

Обрабатывает GET-запрос на получение данных по топ 10 самых доходных магазинов за месяц (id + адреса + суммарная выручка)
При запуске локально endpoint http://127.0.0.1:8080/get_top_stores
Формат выходных данных json
Пример ответа:
{
    "stores": [
        {
            "store_id": 3,
            "address": "Новгород",
            "summ": 300.0
        },
        {
            "store_id": 1,
            "address": "Москва",
            "summ": 200.0
        },
        {
            "store_id": 2,
            "address": "Питер",
            "summ": 200.0
        }
    ]
}
stores[].store_id - идентификатор магазина
stores[].address - адрес магазина 
stores[].summ - сумма продаж

Метод GET /get_top_items

Обрабатывает GET-запрос на получение данных по топ 10 самых продаваемых товаров (id + наименование + количество проданных товаров)
При запуске локально endpoint http://127.0.0.1:8080/get_top_items
Формат выходных данных json
Пример ответа:
{
    "items": [
        {
            "item_id": 10,
            "name": "Товар10",
            "count": 6
        },
        {
            "item_id": 1,
            "name": "Товар1",
            "count": 4
        }
    ]
}
items[].item_id - идентификатор товара для метода POST /post_sales
items[].name - нименование товара
items[].count - количество проданного товара

