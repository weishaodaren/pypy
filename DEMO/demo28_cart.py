# 一个py文件就是一个模块
def addToCart():
    print('添加成功')

def submit():
    print('结算')

def pay():
    print('支付...')
# __all__特殊变量，可以通过这个限制按照*引入的属性方法
__all__=['addToCart','submit']


