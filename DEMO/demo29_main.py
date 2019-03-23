# 创建随机数
# import random
# random.randrange()

# 引入自定义模块
# from demo28_cart import addToCart,submit 方式一
# from demo28_cart import *   方式二
import demo28_cart as m # 方式三
def handleCart():
    # 调用cart的addToCart   
    m.addToCart()
handleCart()
m.submit()

from demo28_cart import *
# pay()

m.pay()