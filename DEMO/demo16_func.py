#方法定义
def test():
    print('test func is called')
# 调用
test()

# 定义一个有参数的方法
def showDetail(id):
    print('这是%d的详情信息'%id)
    return 0,1,54,6,4,65,4,6,4,6,4,6,5,4 # 元组
result=showDetail(3)
print(result)   # 元组







