class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self,name):
        print(self.name+'在吃饭')

#定义在类之外的函数
def show():
    print('我是定义在类之外的函数')

print('----动态绑定属性---')
stu1=Student('张三',20)
stu2=Student('李四',30)
#动态绑定属性
stu2.gender='男'
print(stu2.name,stu2.age,stu2.gender)

print('----动态绑定方法---')
stu1.show=show()
stu1.show