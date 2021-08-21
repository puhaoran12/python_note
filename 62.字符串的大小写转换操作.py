# 字符串的大小写转换操作：
s='hello,hELlo'
# 1.upper() 把字符串中所有字符串都转换成大写字母
print(s.upper())
# 2.lower() 把字符串中所有字符串都转换成小写字母
print(s.lower())
# 3.swapcase() 把字符串中所有大写字母转换成小写字母，把所有小写字母转换成大写字母
print(s.swapcase())
# 4.capitalize() 把第一个字符转换成大写，把其余字符转换为小写
print(s.capitalize())
# 5.title() 把每个单词的第一个字符转换为大写，把每个单词的剩余字符转换成小写
print(s.title())