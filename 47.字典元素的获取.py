# 获取字典中的元素：
# 1.[]  字典名['键']
# 2.get()方法  字典名.get('键')
# 两种方法的区别：
# []如果字典中不存在指定的key，抛出keyError
# get()方法的值，如果指定的键在的字典中不存在，
# 将不会抛出KeyError但返回None，可以将parameter设置为默认值，以便在指定的key不存在时返回
dic={'张三':100,'李四':98,'王五':90}
print(dic['王五'])
#print(dic['赵六'])#KeyError: '赵六'

print(dic.get('张三'))
print(dic.get('赵六'))
print(dic.get('麻七',99))#99是在查找’麻七‘所对的value不存在时，提供的一个默认值,如果存在，则忽略默认值