# 函数的返回值
# 1.如果函数没有返回值（函数执行完毕之后，不需要给调用除提供数据），return可以省略不写
# 2.函数的返回值，如果是1个，直接返回类型
# 3.函数的返回值，如果是多个，返回的结果为元组
#返回多个值
def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

print(fun([10,29,35,40,56,76,57]))
#不返回值
def fun1():
    print('hello')

fun1()
#返回一个值
def fun2(name):
    dic='我叫'+name
    return dic

print(fun2('蒲昊苒'))