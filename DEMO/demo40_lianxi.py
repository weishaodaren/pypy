import mysql.connector as sql
sql=sql.connect(
    host='localhost',
    user='root',
    password='',
    database='xz'
)
yhm=input('请输入用户名')
mm=input('请输入密码')

sqlCursor=sql.cursor()         #游标对象执行sql
Operation="INSERT INTO xz_user (uname,upwd) VALUES (%s,%s)" #占位符
sqlCursor.execute(Operation, (yhm,mm))  #动态传值
sql.commit()
print('插入成功')