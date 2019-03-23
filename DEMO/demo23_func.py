def func(count):
    count+=1
    print('in func count %d'%count)
myCount=1
func(myCount)   #引用类型
print(myCount)  #值类型

def pay(myDic):
    myDic['money']-=10
    print('in pay myDic is ',myDic)
AccountDic={'money':100}    #引用类型
pay(AccountDic)
pay(AccountDic)
pay(AccountDic)
pay(AccountDic)
print(AccountDic)


def pay():
    print('pay func is called')
pay()


# 如在py中定义匿名函数
add=lambda num:print(num)
add(3)

#lambda定义的匿名函数，默认返会：后执行的结果
def test(ope):
    if ope=='+':
        f=lambda:3+5
        f()
        return f()
    elif ope=='-':
        f=lambda:3-5
        f()
        return f()
res=test('+')    
print(res)