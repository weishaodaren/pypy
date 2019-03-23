def getList():
    userList=[]
    def login(uname):
        nonlocal userList #声明 内层可以调用外层
        userList.append(uname)
        print(userList)
    return login
func=getList()
func('a')
func('b')
func('c')