# 字符串的劈分
# 1.split():
#     从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
#     以通过参数sep指定劈分字符串的劈分符
#     通过参数maxsplit指定劈分字符串时的最大劈分次数，在经历最大劈分次数之后，剩余的子串会单独作为一部分
s='hello world python'
print(s.split())

s1='hello|world|python'
print(s1.split(sep='|'))
print(s1.split(sep='|',maxsplit=1))
# 2.rsplit():
#     从字符串的右边开始劈分，默认的劈分字符是空字符串，返回的值都是一个列表
#     以通过参数sep指定劈分字符串的劈分符
#     通过参数maxsplit指定劈分字符串时的最大劈分次数，在经历最大劈分次数之后，剩余的子串会单独作为一部分
