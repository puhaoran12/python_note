# 列表元素的排序操作
# 常见的有两种：
# 1.调用sort()方法。列表中的所有元素默认按照从小到大的顺序进行排序，可以指定reverse=True来进行降序排列
lst=[0, 200, 400, 500, 600, 50, 60, 70, 80, 90, 20]
lst.sort(reverse=True)
print(lst)
# 2.调用内置函数sorted(),可以指定reverse=True，进行降序排列，原列表不发生改变,产生一个新的列表对象
print(sorted(lst,reverse=False))
