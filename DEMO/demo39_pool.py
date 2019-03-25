#连接池
import mysql.connector.pooling as pool

myPool=pool.MySQLConnectionPool(
    pool_size=10,
    host='localhost',
    user='root',
    password='',
    database='xz'
)
#从连接池当中获取一个可用的连接
myConnection=myPool.get_connection()
# 创建游标对象
myCursor=myConnection.cursor()
# 执行sql
myCursor.execute('SELECT * FROM xz_user')
# 结果
print(myCursor.fetchall())