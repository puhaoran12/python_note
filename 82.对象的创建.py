# 对象的创建：对象的创建又称为类的实例化
# 语法：实例名=类名()
class Student:
    native_pace='我是属性'

    #初始化方法
    def __init__(self,name,age):
        # 实例属性
        self.name=name
        self.age=age

    def eat(self):
        print('我是方法')

    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    @classmethod
    def cm(cls):
        print('我使用了classmethod进行修饰，所以我是类方法')

#创建Student类的实例对象
#stu1就是实例对象
stu1=Student('张三',20)
print(stu1.name)
stu1.eat()
Student.eat(stu1)