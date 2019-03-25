class Monestor():
    hp=0
    def run(self):
        print('hp%d小怪兽正在移动'%self.hp)
    def __init__(self,hp):
        self.hp=hp

class Boss(Monestor):
    hp=0
    def run(self):
        print('hp%d大Boss正在移动'%self.hp)

m=Monestor(10)
b=Boss(1222000)
m.run()
b.run()
