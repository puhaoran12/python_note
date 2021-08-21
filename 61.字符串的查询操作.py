#字符串是不可变序列
# 查询方法：
s='hello,hello'
# 1.index() 查找字符串substr第一次出现的位置，如果查找的子串不存在时，则抛出ValueError
print(s.index('lo'))
#print(s.index('k'))#ValueError: substring not found
# 2.rindex() 查找字符串substr最后一次出现的位置，如果查找的子串不存在时，则抛出ValueError
print(s.rindex('lo'))
#print(s.rindex('k'))#ValueError: substring not found
# 3.find() 查找字符串substr第一次出现的位置，如果查找的子串不存在时，则返回-1
print(s.find('lo'))
print(s.find('k'))
# 4.rfind() 查找字符串substr最后一次出现的位置，如果查找的子串不存在时，则返回-1
print(s.rfind('lo'))
print(s.rfind('k'))