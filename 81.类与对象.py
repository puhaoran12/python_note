# 创建类的语法
# class 类名：
#     pass

# 类的组成：类属性，实例方法，静态方法，类方法
# 类属性：直接写在类里的变量
# 方法：类里定义的函数叫方法
# 静态方法：用staticmethod修饰的方法
# 类方法：用classmethod修饰的方法


class Student:
    native_pace='我是属性'

    #初始化方法
    def __init__(self,name,age):
        #实例属性
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


print(Student)
print(id(Student))
print(type(Student))
print(Student().eat())