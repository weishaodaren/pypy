'''
def calc(*num):
    # 遍历元组
    sum=0
    for tmp in num:
        sum+=tmp
    return sum/len(num)
print(calc(15,65,4))
'''
def myDel(myList,index=0):
    myList.pop(index)
    print(type(myList))        
myDel([1,2,3])

def calcFactorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num*calcFactorial(num-1) 
print(calcFactorial(0))