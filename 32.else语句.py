# else语句
#     与else语句配合使用的三种情况：
#     1.if...else...
#     2.while...else...
#     3.for...else...
# 第2,3种情况如果没有遇到break时执行else（循环执行完了执行else），遇到则不会执行

for item in range(3):
    pwd=input('请输入密码：')
    if pwd=="8888":
        print('密码正确！')
        break
    else:
        print('密码不正确！')
else:
    print('对不起，三次密码输入均不正确')