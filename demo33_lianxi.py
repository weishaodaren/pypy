class Car():
    def drive(self):
        print(self.brand+'正在行驶')
    brand=''
    def __init__(self,id):
        self.brand=id
t=Car('qq')
print(t.brand)
t.drive()