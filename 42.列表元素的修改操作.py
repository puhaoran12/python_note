lst=[0, 10, 30, 40, 50, 60, 70, 80, 90, 20]
print(id(lst))
#为指定索引的元素赋予一个新值
lst[3]='hello'
print(lst,id(lst))
#为指定的切片赋予一个新值
lst[1:3]=[200,400,500,600]
print(lst,id(lst))
