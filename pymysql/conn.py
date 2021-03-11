#! /usr/bin/python3
import pymysql
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql.functions import user

# engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('root', 'Root123!@#', 'localhost', '3306', 'emos'))
# print("pass")

# sql_query = 'SELECT * From tb_permission'
# df_read = pd.read_sql_query(sql_query, engine)
# print(df_read)

config = {
    'host':'127.0.0.1',#'localhost'
    'port':3306, #MySQL默认端口
    'user':'root', #mysql默认用户名
    'password':'Root123!@#',
    'database':'emos', #数据库
    'charset':'utf8mb4',   
    }

db = pymysql.connect(**config)

cursor = db.cursor()

sql = "select * from tb_permission \
    "
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
except:
    print("failed")
print('pass')
