# 集合是可变序列
# 创建方式：(元素之间用逗号,隔开)
# 1.直接{}
s={'hello',1,1,2,4,4}#集合中的元素不能重复
print(s)
print(type(s))
# 2.使用内置函数set{}
s1=set(range(6))
print(s1)
print(type(s1))
#将列表转换为集合
s2=set([1,2,3,4,4,5,6,6])
print(s2)
print(type(s2))
#将元组转换成集合
s3=set((1,2,3,65,5,6,6,76))#集合中元素是无序的
print(s3)
print(type(s3))

s4=set('python')
print(s4)
print(type(s4))

#定义空集合
s5={}
print(type(s5))

s6=set()
print(type(s6))
