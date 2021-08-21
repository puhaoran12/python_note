# 内置函数zip()
# 用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表
# 将可迭代的对象：可以用作for循环的对象
items=['Fruits','Books','Others']
prices=[96,78,85,100,30]

d={item:price for item,price in zip(items,prices)}
print(d,type(d))
#组注意：键和值个数不一样时，以少为基准

for item in zip(items,prices):
    print(item)
    
print(zip(items,prices))