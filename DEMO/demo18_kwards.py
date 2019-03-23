# 关键字参数
def add(num1,num2):
    print(num1,num2)
    print(num1+num2)
add(1,1)
add(num2=5,num1=3)

# 默认值参数
def test(host,port=3306):   #默认端口
    print(host,port)
test('176.50.2.30')
test('localhost',7878)


