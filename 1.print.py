# print()函数可以输出哪些内容？
# 1.数字
print(123)
# 2.字符串
print("hello")
print('hello')
# 3.含有运算符的表达式
print(1+3)
print("1"+"3")
# print()函数可以将内容输出的目的地
# 1.显示器
# 2.文件
#注意点：1所指定的盘符存在 2.使用file=
fp=open('E:/untitled7/python笔记/test.txt','a+')#文件地址不能用 \ ,只能用 /  .a+表示如果test文件不存在则创建，存在则将内容加在而文件已有内容后面
print('hello我是1.print的测试文件',file=fp)
fp.close()
# print()函数的输出形式
# 1.换行
# 2.不换行
print('hello','world')