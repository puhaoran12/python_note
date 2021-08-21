#break语句：用于结束循环结构，通常与分支结构if一起使用
#满足一个分支则跳出（结束循环）
for i in range(1,100):
    if i==60:
        break
print(i)

a=0
while a<100:
    if a==37:
        break
    a+=1
print(a)