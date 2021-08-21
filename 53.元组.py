#元组是不可变序列
#元组的创建方式：
#1.用()定义，元素间逗号,隔开
t=('python','world',98)
print(t)
print(type(t))
# 2.使用内置函数tuple()
t1=tuple(('python','world',98))
print(t1)
print(type(t1))
# 3.只包含一个元组的元素需要使用逗号和小括号
t3=('python',)
print(t3)
print(type(t3))

#空元组
t4=()
t5=tuple()
print(t4)
print(t5)