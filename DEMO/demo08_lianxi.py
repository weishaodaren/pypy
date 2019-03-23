myDict={}
myDict['price']=float(input('商品单价：'))
myDict['name']=input('商品名称：')
myDict['count']=int(input('商品数量：'))
print(myDict)

totalPrice=myDict['price']*myDict['count']
# print(totalPrice)
print('%s花费%f'%(myDict['name'],totalPrice))
