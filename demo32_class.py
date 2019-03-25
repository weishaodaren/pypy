# 定义一个类
class Ticket():
    oid=0
    content=''
    # 定义构造函数 可以在构造函数中完成数据初始化工作
    def __init__(self,id,ct):
        self.oid=id
        self.content=ct
    def calcPrice(self):
        print('当前小票总价是80')
# 调用类 类的实例化 (将一个类变成对象或者实例的过程)
t=Ticket(100,'贪吃粑粑')
print(t.oid)
t.calcPrice()





