a,b=10,20
print('a大于b吗？',a>b)
print('a小于b吗？',a<b)
print('a小于等于b吗？',a<=b)
print('a大于等于b吗？',a>=b)
print('a等于b吗？',a==b)
print('a不等于b吗？',a!=b)

print('----------------')
# 变量由三个部分组成：标识id,类型，值
# 比较运算符中，比较的是值
# 比较对象标识使用 is
a=10
b=10
print(id(a))
print(a==b) #True 说明a,b的value相等
print(a is b) #True 说明a,b的id相等
print(a is not b)