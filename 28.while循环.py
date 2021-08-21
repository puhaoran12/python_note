# 语法结构：
#     while 条件表达式：
#         条件执行体（循环体）
# 选择结构的if与循环结构while的区别
#     if是判断一次，条件为True执行一行
#     while是判断N+1次，条件为True执行N次
i=0
c=0
while i<10:
    c+=i
    print(c)
    i+=1

a=b=0
while a<101:
    if a%2==0:
        b+=a
    a+=1
print('1-100之间的偶数和：'+str(b))


