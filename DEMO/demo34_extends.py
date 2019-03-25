# 完成继承和多态处理
class Order():
    oid=0
    price=0
    def __init__(self,oid,price):
        self.oid=oid
        self.price=price
# 将order数理化一个对象
myOrder=Order(654,1)
print(myOrder.oid)

# 添加实现外卖订单---继承
class DeliveryOrder(Order):
    deliverySender=''   #保存配送人员信息
    def __init__(self,sender,id,price):
        self.deliverySender=sender
        # 方案1
        # self.oid=id
        # self.price=price
        # 方案2  通过super方法得到父类
        super().__init__(id,price)
# 将一个类经行实例化的过程，如果 没有定义构造函数，找父类构造函数处理
dOrder=DeliveryOrder('xiaohei',1,100)
print(dOrder.deliverySender)
print(dOrder.price,dOrder.oid)
