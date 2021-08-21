# 列表元素的增加操作：
lst=[10]
print('添加元素之前',lst,id(lst))
print('-----添加元素之前--------')
# 1.append() 在列表的末尾添加一个元素
lst.append(100)
print(lst,id(lst))
# 2.extend() 在列表的末尾至少添加一个元素
lst.extend(lst)#将一个列表中的元素插入到列表的末尾
print(lst,id(lst))
# 3.insert() 在列表的任意位置添加一个元素
lst.insert(1,90)#括号中依次为：索引，元素
print(lst,id(lst))
# 4.切片 在列表的任意位置添加至少一个元素（相当于替换掉切片中的元素）
lst2=["hello",'ok']
lst[1:]=lst2
print(lst,id(lst))

