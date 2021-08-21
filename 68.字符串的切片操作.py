#字符串是不可变类型，切片都将产生新的对象
s1='hello'
s2='python'
s3='pythonpythonpython'
print(s1[:3])#默认从索引为0开始
print(s2[2:])#默认切片到最后
print(s1+'!'+s2)
print(s3[2:9:2])#步长为2