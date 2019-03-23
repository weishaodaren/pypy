#定义
myDict={ 
    'stuName':"zhangsan",
    'stuAge':20,
}
print(myDict,type(myDict))

#读
print(myDict['stuName'])
print(myDict.get('stuAge'))

# 写
myDict['stuName']='草您奶'
print(myDict)

#添加
myDict['className']='搞您奶奶个腚'
print(myDict)

#删除
myDict.pop('stuAge')
print(myDict)


