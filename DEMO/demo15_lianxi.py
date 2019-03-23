import random
ran=random.randrange(100)
# print(ran)

while True:
    num=int(input('输入一个数字：'))
    if num>ran:
        print('大')
    elif num<ran:
        print('小')
    else:
        print('YES')
        break










