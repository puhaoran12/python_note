# 语法结构：
#     if 条件表达式：
#         条件执行体
money=1000
a=int(input('请输入取款金额：'))
if a<=money:
    money=money-a
    print('取款成功，余额为：',money)