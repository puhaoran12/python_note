def calc(a,b):#a,b称为形式参数，简称形参，形参的位置是在函数定义处
    c=a+b
    return c
#1.根据形参对应的位置进行传递实参传递
result=calc(10,20) #10，20称为实际参数，简称实参，实际参数的位置是函数的调用处
print(result)
#2.根据形参名称进行实参传递
result=calc(b=10,a=20)# =左侧的变量名称称为关键字参数
print(result)