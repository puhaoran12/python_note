# for-in循环
#     in表达从（字符串，序列等）中依次取值，又称遍历
#     for-in遍历的对象必须可以迭代对象
# for-in的语法结构：
#     for 自定义的变量 in 可迭代对象：
#         循环体
print('遍历字符串')
for s in 'adfafa':
    print(s)

for i in range(10):
    print(i)
    print(2)

#如果在循环体中不需要使用到自定义变量，可将自定义变量写成’_‘
for _ in range(5):
    print("可乐")

c=0
for i in range(101):
    if i%2==0:
        c+=i
print('1-100之间的偶数和：'+str(c))
