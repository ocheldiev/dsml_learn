import sqlite3

print("Begin")
#""" Подготовка тестовых данных"""
storeTestData=(
    ('Москва',), 
    ('Питер',), 
    ('Новгород',), 
    ('Владикавказ',), 
    ('Воронеж',), 
    ('Липецк',), 
    ('Ярославль',), 
    ('Владимир',), 
    ('Иваново',), 
    ('Кострома',), 
    ('Астрахань',), 
    ('Орел',), 
    ('Псков',), 
    ('Севастополь',), 
    ('Еще какой-то город',)
)
itemTestData=(
    ('Товар1',10),
    ('Товар2',20),
    ('Товар3',30),
    ('Товар4',40),
    ('Товар5',50),
    ('Товар6',60),
    ('Товар7',70),
    ('Товар8',80),
    ('Товар9',90),
    ('Товар10',10),
    ('Товар11',110),
    ('Товар12',120),
    ('Товар113',130),
    ('Товар14',140),
    ('Товар115',150),
    ('Товар16',160),
)

salesTestData=(
    ('2022-11-20',1,1),
    ('2022-11-20',1,2),
    ('2022-11-20',2,3),
    ('2022-11-20',2,1),
    ('2022-11-20',3,2),
    ('2022-11-20',4,3),
    ('2022-11-20',5,1),
    ('2022-11-20',6,2),
    ('2022-11-20',7,3),
    ('2022-11-20',8,1),
    ('2022-11-20',9,2),
    ('2022-11-20',9,3),
    ('2022-11-20',1,1),
    ('2022-11-20',1,2),
    ('2022-11-20',2,3),
    ('2022-11-20',3,1),
)

conn = sqlite3.connect('shop.db')
#SQLite имеет всего четыре примитивных типа данных: INT, REAL, TEXT и BLOB
cur = conn.cursor()
#""" Создаем и заполняем таблицу store - магазины торговой сети """
cur.execute("DROP TABLE IF EXISTS store")
cur.execute("CREATE TABLE store(id INTEGER PRIMARY KEY AUTOINCREMENT, address TEXT)")
cur.executemany("INSERT INTO store (address) VALUES(?)", storeTestData)
#""" Создаем и заполняем таблицу item товарные позиции (уникальные наименования) """
cur.execute("DROP TABLE IF EXISTS item")
cur.execute("CREATE TABLE item(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL)")
cur.executemany("INSERT INTO item (name,price) VALUES( ?, ?)", itemTestData)
#""" Создаем и заполняем таблицу sales - продажи"""
cur.execute("DROP TABLE IF EXISTS sales")
cur.execute("CREATE TABLE sales(id INTEGER PRIMARY KEY AUTOINCREMENT, sale_time TEXT,item_id INT,store_id INT)")
cur.executemany("INSERT INTO sales (sale_time,item_id,store_id) VALUES( ?, ?, ?)", salesTestData)

conn.commit()
cur.close()
print("End")
