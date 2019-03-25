# 多态实现
class Car():
    def drive(self):
        print('汽车正在加速')
class SUV(Car):
    def drive(self):
        print('我是越野车')

myCar=Car()
mySUV=SUV()
# 调用方法
myCar.drive()
mySUV.drive()