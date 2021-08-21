# 列表元素的删除操作：
lst=[00,10,20,30,40,50,60,70,80,90,20]
# 1.remove() 一次只删除一个元素；重复元素值删除第一个；元素不存在抛出ValueError
lst.remove(20)#从列表中移除一个元素，如果有重复元素只移除第一个元素
print(lst)
#lst.remove(100)#x not in list
print(lst)
# 2.pop() 删除一个指定索引位置上的元素；指定索引不存在抛出IndexError；不指定索引，删除列表中最后一个元素
lst.pop(1)
print(lst)
#lst.pop(10)#pop index out of range
print(lst)
lst.pop()
print(lst)
# 3.切片 一次至少删除一个元素
print('------切片操作-删除至少一个元素，将产生一个新的列表对象-----')
new_list=lst[1:3]
print('原列表',lst,id(lst))
print('切片后的列表',new_list,id(new_list))

'''不产生新的列表对象，而是删除原列表中的内容'''
lst[1:3]=[]
print(lst)
# 4.clear() 清空列表
print(lst.clear(),id(lst))
# 5.del 删除列表
del lst
print(lst)#name 'lst' is not defined