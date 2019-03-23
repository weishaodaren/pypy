def log(func):                  #装饰器
    def handle(*args):
        print('有个方法被调用了')
        func(*args)
    return handle

@log
def login(uname):
    print(uname,'login succ')
login('Kitty')


