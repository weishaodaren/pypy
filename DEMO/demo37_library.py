# 标准库
import math     #数学处理   三角函数 取整。。。
import random  #创建随机数字
import time     #处理时间和日期
import os.path  #处理路径

print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.exists('C:/xampp'))   #判断文件是否存在


print(time.localtime())
print(time.strftime('%y %m %d %H %M %S'))
# %y %m %d %H %M %S


print(random.randrange(50,100))
print(random.choice(['a','b','c'])) #多个选择

price=40.2
print(math.ceil(price))     #向上取整


import json
# json序列化 数据变成json格式字符串
# json反序列化 
myDict={'stuName':'John','stuAge':80}
myStr= json.dumps(myDict)  
print(myStr,type(myStr))

print(json.loads(myStr),type(json.loads(myStr)))