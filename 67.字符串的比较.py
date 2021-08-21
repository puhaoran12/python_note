# 字符串比较操作符:>，>=，<，<=，==，!=
# 比较规则:首先比较两个字符串的第一个字符,如果相等则继续比较下一个字符，依次比较下去，直到两个字符串中的字符不相等时,其比较的结果是两个字符串的比较结果,两个字符串中的所有字符将不再比较
# 比较原则: 两个字符进行比较,比较的是其ordinal value(原值),调用内置函数ord可以得到指定字符的ordinal value,和内置函数ord对应的内置函数chr,调用内置函数chr时指定ordinal value可以得到其对应的字符
print('apple'>'app')
print('apple'>'banana')
print(ord('a'),ord('b'))
print(chr(97),chr(98))