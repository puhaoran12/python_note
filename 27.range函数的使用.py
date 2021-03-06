#range()函数用于生成一个整数序列
#range()的三种创建方式
'''第一种创建方式，只有一个参数（括号中只给一个数）'''
r=range(10)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，默认从0开始，默认相差1为步长
print(r) #range(0,10)
print(list(r)) #用于查看range对象中的整数序列   -->list是列表的意思

'''第er种创建方式，只有二个参数（括号中只给二个数）'''
r=range(1,10) #指定了起始值，从1开始，到10结束（不包含10），默认步长为1
print(list(r))

'''第3种创建方式，只有3个参数（括号中只给3个数）'''
r=range(1,10,2) #range(开始值,终止值,步长)
print(list(r))
#判断是是否在这个序列中
print(10 in range(1,10,2))