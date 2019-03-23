# 嵌套函数作用域
def outer():
    count=0
    def inner():    #__closure__ 闭包
        nonlocal count
        print('inner func is called')
        print('count is %d'%count)
        # nonlocal count 声明要提前
        count+=1
    return inner
func=outer()
func()
func()
func()


# 内置作用域  build-in  int()
myNum='3011'
print(int(myNum))

def int(arg1):
    print('----'+arg1)
print(int(myNum))
