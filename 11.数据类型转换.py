name='张三'
age=20
print(type(name),type(age))
#print('我叫'+name+',今年'+age+'岁')#当将str类型与interesting类型连接时，报错。解决方案：类型转换
print('我叫'+name+',今年'+str(age)+'岁')#将int类型通过str()函数转换成str类型

print('-------使用str()函数将其他类型转换成str类型---------')
a=10
b=2.2
c=False
print(type(a),type(b),type(c))
print(str(a),type(str(a)))
print(str(b),type(str(b)))
print(str(c),type(str(c)))

print('-----使用int()函数将其他的类型转换为int类型--------')
s1='123.3'
s2=98.4
s3=True
s4='77'
s5='hello'
print(type(s1),type(s2),type(s3),type(s4),type(s5))
#print(int(s1),type(int(s1)))
print(int(s2),type(int(s2)))#抹零取整
print(int(s3),type(int(s3)))
print(int(s4),type(int(s4)))
#print(int(s5),type(int(s5)))
#将字符串转换为int类型时，字符串必须是数字串，且不能为小数串

print('---------使用float函数，将其他数据类型转换成float类型-------')
s1='123.3'
s2=98
s3=True
s4='77'
s5='hello'
print(type(s1),type(s2),type(s3),type(s4),type(s5))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(s3),type(float(s3)))
print(float(s4),type(float(s4)))
print(float(s5),type(float(s5)))
#
