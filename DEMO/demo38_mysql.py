# 引入数据库工具
import mysql.connector as sql

myConnect=sql.connect(
    host='localhost',
    user='root',
    password='',
    database='xz'
)
# print(myConnect)
# 创建游标对象 cursor
myCursor=myConnect.cursor()

# myOperation="SELECT * FROM xz_user"
myOperation="INSERT INTO xz_user (uname,upwd) VALUES ('好嗨哦','123456')"
myCursor.execute(myOperation)   #游标 执行sql语句
myConnect.commit()                                  #除 查找外 增删改 都要这句话
# res=myCursor.fetchall()     #获得所有结果
# print(res,type(res))