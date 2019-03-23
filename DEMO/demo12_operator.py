#位运算  & | ~ ^ <<  >> 将数字按照二进制的方式 每一位进行运算 
num0=int('00111100',2)
num1=int('00100110',2)
print(num0,num1)
print(num0&num1)    
print(num0|num1)    

# 成员运算符    in/not in
# 在数组 字典 元祖当中判断某个元素是否存在
myList=[1,3,2]
print(3 in myList)
print(5 not in myList)

myDict={'age':24,'name':'Terry'}
print(24 in myDict) #F
print('age' in myDict) #T


# 身份运算符
score1=80
score2=score1
print(id(score1),id(score2))
score1=90
print(id(score1),id(score2))

#引用类型
scoreList=[100,200]
myScoreList=scoreList
print(myScoreList,scoreList)
scoreList[0]=90
print(myScoreList is scoreList)









