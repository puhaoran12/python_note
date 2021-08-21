#语法：try...except 错误类型 ...

try:
    a=int(input('请输入第一个整数：'))
    b=int(input('请输入第二个整数：'))
    result=a/b
    print('结果：',result)
except ZeroDivisionError:
    print('对不起，除数不能为0')
print('程序结束')