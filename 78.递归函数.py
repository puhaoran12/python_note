# 递归函数：如果在一个函数的函数体内调用了该函数本身，这个函数就称为递归函数
# 递归的组成部分：递归调用与递归终止条件
# 递归的调用过程：每递归调用一次函数，都会在栈内存分配一个栈帧，每执行完一次函数，都会释放相应的空间
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(6))
#斐波那契数列
def fun(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fun(n-1)+fun(n-2)

print(fun(6))