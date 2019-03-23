# 常见的数据类型
age=20
price=30.5
isMember=False
myData=3+2j

print(age,type(age))            #<class 'int'>
print(price,type(price))        #<class 'float'>
print(isMember,type(isMember))  #<class 'bool'>
print(myData,type(myData))      #<class 'complex'>

# 格式化输出    %d 整数  %f浮点数  %s字符串
print('age is %d '%age)
chineseScore=60
mathScore=100
print('语文成绩%d数学成绩%d' %(chineseScore,mathScore))

print('age is '+str(age))   #str 转字符串

#字符串
stuName='JohnReese'
stuAddr='海淀区'
stuMsg='这是个傻屌，他就是傻錷夁'
print(stuName,type(stuName))
print(stuAddr,type(stuAddr))
print(stuMsg,type(stuMsg))

averageScore=input('请输入您的成绩')
print(averageScore,type(averageScore))

print(int(averageScore))









































