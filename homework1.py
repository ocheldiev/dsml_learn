import aiohttp
from aiohttp import web
#import nest_asyncio
#nest_asyncio.apply()
#import sqlite3
import aiosqlite as lite
from datetime import date

async def get_store_db():
    conn=await lite.connect("shop.db")
    cursor = await conn.cursor()
    sql="select * from store;"
    await cursor.execute(sql)
    rec = await cursor.fetchall()
    await cursor.close()
    dic={}
    tmp_lst=[]
    for i in rec:
        tmp_lst.append({"store_id":i[0],"address":i[1]})
    dic["stores"]=tmp_lst
    await conn.close()
    return dic

async def get_item_db():
    conn=await lite.connect("shop.db")
    cursor = await conn.cursor()
    sql="select * from item;"
    await cursor.execute(sql)
    rec = await cursor.fetchall()
    await cursor.close()
    dic={}
    tmp_lst=[]
    for i in rec:
        tmp_lst.append({"item_id":i[0],"name":i[1],"price":i[2]})
    dic["items"]=tmp_lst
    await conn.close()
    return dic

async def get_top_store_db():
    conn=await lite.connect("shop.db")
    cursor = await conn.cursor()
    sql="select * from\
        (\
            select *  from(\
                select st.id, st.address,sum(i.price) summ, ROW_NUMBER () OVER (PARTITION BY st.id) rownum from store st\
                join sales s on s.store_id = st.id\
                join item i on s.item_id = i.id\
                group by st.id, st.address\
            ) order by summ desc\
        )where rownum <= 10;"#написать запрос с джоином
    await cursor.execute(sql)
    rec = await cursor.fetchall()
    await cursor.close()
    dic={}
    tmp_lst=[]
    for i in rec:
        tmp_lst.append({"store_id":i[0],"address":i[1],"summ":i[2]})
    dic["stores"]=tmp_lst
    await conn.close()
    return dic

async def get_top_item_db():
    conn=await lite.connect("shop.db")
    cursor = await conn.cursor()
    sql="select * from\
        (\
            select * from(\
                select i.id, i.name,count(*) cnt, ROW_NUMBER () OVER (PARTITION BY i.id) rownum from item i\
                join sales s on s.item_id = i.id\
                group by i.id, i.name\
            ) order by cnt desc\
        )where rownum <= 10;"#написать запрос с джоином
    await cursor.execute(sql)
    rec = await cursor.fetchall()
    await cursor.close()
    dic={}
    tmp_lst=[]
    for i in rec:
        tmp_lst.append({"item_id":i[0],"name":i[1],"count":i[2]})
    dic["items"]=tmp_lst
    await conn.close()
    return dic

routes = web.RouteTableDef()

@routes.post('/post_sales')
async def post_sales_handler(request):
    #data = await request.post()
    today = date.today()
    Data = await request.json()
    #store = post["store"]["id"]
    #item = post["store"]["item"]
    conn=await lite.connect("shop.db")
    cursor = await conn.cursor()
    #print(Data)
    #print(((str(today),int(Data["item_id"]),int(Data["store_id"]))))
    salesData=((str(today),int(Data["item_id"]),int(Data["store_id"])))
    await cursor.execute("INSERT INTO sales (sale_time,item_id,store_id) VALUES( ?, ?, ?)", tuple(salesData))
    await conn.commit()
    await cursor.close()
    await conn.close()
    return web.Response(text="OK")

@routes.get('/get_stores')
async def get_store_handler(request):
    s=await get_store_db()
    #return web.Response(text=s) 
    return web.json_response(s)
@routes.get('/get_items') 
async def get_items_handler(request):
    s=await get_item_db()
    return web.json_response(s)
@routes.get('/get_top_stores') 
async def get_top_stores_handler(request):
    s=await get_top_store_db()
    return web.json_response(s)
@routes.get('/get_top_items') 
async def get_top_items_handler(request):
    s=await get_top_item_db()
    return web.json_response(s)


#обрабатывает GET-запрос на получение всех товарных позиций
#обрабатывает GET-запрос на получение всех магазинов 
#обрабатывает POST-запрос с json-телом для сохранения данных о произведенной продаже (id товара + id магазина)
#обрабатывает GET-запрос на получение данных по топ 10 самых доходных магазинов за месяц (id + адреса + суммарная выручка)
#обрабатывает GET-запрос на получение данных по топ 10 самых продаваемых товаров (id + наименование + количество проданных товаров)



app = web.Application()
app.add_routes(routes) # добавляем в приложение пути, которое оно должно обслуживать
web.run_app(app) # запуск приложения
