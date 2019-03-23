# 装饰器：函数、方法

# 定义装饰器函数
def checkLogin(func):
    def handle():
        # 实现执行扩展功能
        print('检查用户登录')
        func()
    return handle



# 功能扩展 ：验证用户是否登录
# OCP Open Close Principle 扩展开放，修改关闭
@checkLogin
def addToCart():
    print('添加成功!')
addToCart()




