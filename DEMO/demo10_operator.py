# 算术运算 +-*/% 
num1=10
num2=3
print(num1+num2,type(num1+num2))
print(num1%num2)    #取余
print(num1//num2)   #商下取整
print(num1**num2)   #num1的num2次幂

#比较运算 > >= < <= == !=
print(num1==num2)
myList1=[534,465,654]
myList2=[534,462,654]
print(myList1>myList2)

myName1='zhangsan'
myName2='zhangsi'
print(myName1>myName2)


#逻辑运算  and or not
# 与运算
cScore=100
mScore=109
print(cScore==100 and mScore==100)

#或运算 有一个为真 就为真
print(True or False)

#非运算 取反
print(not True)

# 赋值运算
age=20
myList3=[12,13]
[score1,score2]=myList3
print(score1,score2)
score3=score4=44
print(score3,score4)
