# 判断字符串操作
s='hello,python'
# 1.isidentifier() 判断指定的字符串是不是合法的标识符
print('1',s.isidentifier())
# 2.isspace() 判断指定的字符串是否全部由空白字符组成（回车，换行，水平制表符）
print('2',s.isspace())
# 3.isalpha() 判断指定的字符串是否全部由字母组成
print('3','sfef'.isalpha())
# 4.判断指定的字符串是否全部由十进制的数字组成
print('4','13235'.isdecimal())
# 5.判断指定的字符串是否全部由数字组成
print('5','34'.isnumeric())
# 6.判断指定字符串是否全部由字母和数字组成
print('6','s43fef'.isalnum())