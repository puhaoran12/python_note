# 获取字典试图：
dic={'张三':100,'李四':98,'王五':90}
# 1.keys() 获取字典中所有key
keys=dic.keys()
print(keys)
print(type(keys))
#类型转换
print(list(keys))
# 2.values() 获取字典中所有的values
values=dic.values()
print(values)
print(type(values))
# 3.items() 获取字典中所有key，value对
items=dic.items()
print(items)
print(type(items))
#类型转换
print(list(items))

