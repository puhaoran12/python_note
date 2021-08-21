# 语法：for 自定义变量 in 字典名

dic={'张三':100,'李四':98,'王五':90}
for item in dic:
    print(item,dic[item],dic.get(item))