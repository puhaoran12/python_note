# 键的判断：
# in 或 not in   语法：字符串 in 字典名
dic={'张三':100,'李四':98,'王五':90}
print('张三' in dic)

#新增元素
dic['陈六']=100
print(dic)

#修改元素
dic['陈六']=0
print(dic)

# 字典元素的删除
# del 字典名['键']
del dic['张三']
print(dic)
dic.clear()#清空字典中所有元素
print(dic)


