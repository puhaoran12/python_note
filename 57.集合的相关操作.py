#判断操作做：in 或 not in
s={10,20,30,40,50}
print(10 in s)
print(100 in s)
# 新增操作：
# 1.调用add()方法，一次添加一个元素
s.add(80)
print(s)
# 2.调用update()方法至少添加一个元素
s.update({200,400},['python'],'pyhton')
print(s)
# 删除操作：
# 1.调用remove()方法,一次删除一个指定元素,如果指定的元素不存在抛出KeyError
# 2.调用discard()方法,一次删除一个指定的元素,如果指定的元素不存在不抛出异常
# 3.调用pop()方法,一次删除一个任意元素 #pop()是没有参数的
# 4.调用clear()方法，清空集合