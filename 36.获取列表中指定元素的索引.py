lst=['hello','world',98,'hello']
# 获取列表指定元素的索引：
# 语法：列表名.index(元素)
# 1.如果列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
print(lst.index('hello'))
# 2.如果查询的元素在列表中不存在，则会抛出ValueError
# 3.还可以在指定的start和stop之间进行查询
print(lst.index('hello',1,4))#查找索引在1-4之间的hello
