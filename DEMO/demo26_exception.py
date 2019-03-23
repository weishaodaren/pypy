try:
    print(asdada)
except NameError:
    print('iuhe')
finally:
    print('987')
print('sasdad')

'''
#方法1
try:
    score=int(input('请输入...'))
    print('score is'+score)
except Exception as msg:
    print('错啦',msg)
#方法2 
try:
    score=int(input('请输入...'))
    print('score is'+score)
except (TypeError,ValueError):
    print('出错')
'''
try:
    score=int(input('请输入...'))
    print('score is'+score)
except ValueError:
    print('值有问题')
except TypeError:
    print('数据类型有问题')





