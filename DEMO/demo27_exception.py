# 完成错误触发信息的自定义和接收
# raise as
try:
    #代码处理
    raise(TypeError('自定义信息内容'))
except TypeError as msg:
    print('error',msg)



try:
    arr=[13,2,1]
    print(arr[10])
except Exception as err:
    print('error',err)
















