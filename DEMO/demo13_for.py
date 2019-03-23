#在python实现循环的各种方式
myList=[354,64,64,498,4,64,9,648,23,
684,5,68,4,68,46,84,68,4,96,8,]
for tmp in myList:
    print(tmp)

print(range(3)) #range方法可以生成从start,end截至的序列，默认从0开始
print(range(1,10,2))
for tmp in range(len(myList)):
    print(tmp,myList[tmp])
    # print('呜呼拉闸')


count=0
while count<10:
    count+=1
    print(count)

while True:
    count+=1
    print(count)
    if count>=10:
        break

day=0
while day<31:
    day+=1
    print('今天是%d号'%day)
    if day==10:
        continue 
    print('省吃俭用')
       
        



























