# try...except...else...结构
#     如果try块中没有抛出异常，则执行else块，如果try中抛出异常，则执行except块
try:
    a=int(input('请输入第一个整数：'))
    b=int(input('请输入第二个整数：'))
    result=a/b
except BaseException as e:
    print('出错了',e)
    print(e)
else:
    print('结果：',result)
# try...except...else...finally结构
#   finally块无论是否发生异常都会被执行，长能用来释放try块中申请的资源
try:
    a=int(input('请输入第一个整数：'))
    b=int(input('请输入第二个整数：'))
    result=a/b
except BaseException as e:
    print('出错了',e)
    print(e)
else:
    print('结果：',result)
finally:
    print('无论是否产生异常，总会被执行的代码')
print('程序结束')