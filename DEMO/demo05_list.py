# list 存储有序序列
myList=[21,354,7638]

# 读取
print(type(myList))
print(myList[0],myList[-2])

# 修改
myList[0]=68684638796684
print(myList)

# 常见api
scoreList=[80,70,90]
# 添加
scoreList.append(999)
scoreList.insert(0,888)     #第一个参数下标位置，插入第二个参数的数据
scoreList.pop(0)             #没有参数，默认删除最后一个元素
print(scoreList)






