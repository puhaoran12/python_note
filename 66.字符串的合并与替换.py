# 字符串替换replace()：第1个参数指定被替换的子串，第2个参数指定替换字串的字符串，该方法返回替换后得到的字符串，替换前的字符串不发生变化，调用该方法时可以通过第3个参数指定最大替换次数
s='hello,python,python,python'
print(s.replace('python','java'))
print(s.replace('python','java',2))
# 字符串的合并join():将列表或元组中的字符串合并成一个字符串
lst=['hello','java','python']
print('|'.join(lst))
print('*'.join('python'))