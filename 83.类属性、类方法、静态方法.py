# 类属性：类中方法外的变量称为类属性，被该类的所有对象所共享
#调用方法：类名.属性名
# 类方法：使用@classmethod修饰的方法，使用类名直接访问的方法
#调用方法：类名.类方法()
# 静态方法：使用@staticmethod修饰的方法，使用类名直接访问的方法
#调用方法：类名.静态方法()

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

print(Student.native_pace)
stu1=Student('张三',20)
stu2=Student('李四',30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace='云南'
print(stu1.native_pace)
print(stu2.native_pace)

Student.cm()
Student.method()
