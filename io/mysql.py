
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('数据库连接字符串')


Base = declarative_base()
TableName = 'aa'

class MyTable(Base,TableName):
    __tablename__ = TableName
    id = Column(Integer, primary_key=True)
    name = Column(String(255))



# MySQL连接池是一个用来管理数据库连接的技术，它允许我们在应用程序中预先创建一定数量的数据库连接，而不是每次需要和数据库通信时都新建一个连接。
# 这消除了频繁连接和断开数据库所需的开销，同时可以更好地管理连接资源。
# 注意: 池子中的链接不会重新生成, 只是存放固定连接数的一个池子 【理解】链接池是一个取用归还的过程不涉及链接关闭,

import mysql.connector.pooling

pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="my_pool",
    pool_size=5,
    pool_reset_session=True,
    host="localhost",
    database="my_database",
    user="my_username",
    password="my_password"
)

connection = pool.get_connection()
cursor = connection.cursor()
cursor.execute("SELECT * FROM my_table")
result = cursor.fetchall()
connection.close()

# 上述代码中，我们首先从连接池中获取一个连接，然后使用cursor()方法创建一个MySQL游标。接着，我们可以使用游标执行SQL查询语句，并使用fetchall()方法获取结果。
# 当使用完连接后，我们需要使用close()方法关闭连接，将其归还给连接池【链接池的close方法是将链接归还给连接池, 而不是将该链接关闭】。