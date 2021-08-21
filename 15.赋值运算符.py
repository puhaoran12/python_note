#赋值运算符：运算顺序是从右到左
i=3+4
print(i)
a=b=c=10
d=10
e=a
print(a,id(a))
print(b,id(b))
print(c,id(c))
print(d,id(d))
print(e,id(e))

print('-----解包赋值-----')
a,b=2,6
print(a,b)
a,b=b,a
print(a,b)