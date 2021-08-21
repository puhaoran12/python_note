# 单引号和双引号的字符串必须在一行
# 三引号定义的字符串可以分布在连续的多行
str1='人生苦短，我用python'
str2="人生苦短，我用python"
str3="""人生苦短，
我用python"""

str4 = '''人生苦短，
我用python'''
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))