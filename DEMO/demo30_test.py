# # 准备当前的模块中 调用另外一个包中的模块方法
# from user.order import *
# getOrderList()

# from user import order
# order.getOrderList()

from user import *
order.getOrderList()
infomation.getAvatar()