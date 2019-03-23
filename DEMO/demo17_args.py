# 可变长参数
def connect(*args):
    print(args,type(args))
connect('loalhost',3306)
connect('loalhost',3306,'xuezi')

# 可变长参数写法 2
def link(**args):
    print(args,type(args))
link(host='localhost',port=3306)

