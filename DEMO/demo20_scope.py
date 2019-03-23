# 作用域
# python L(local局部)E(embed嵌套)G(global全局)B(bulitin)

def func():
    num=10
    print('in func num is %d'%num)
func()
# print(num) 局部变量不可以在外面调用，不造成全局污染

count=0
def modifyCount():
    # 注意  可读 但如果在py内部方法修改全局变量的值，通过global来告诉这是一个全局
    global count
    count=2
    count+=1
    print('in modifyCount: count is %d'%count)
modifyCount()
print('after modify count is %d'%count)


