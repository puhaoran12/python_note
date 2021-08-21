# 继承
# 语法格式：
# class 子类类名(父类1,父类2...):
#     pass
# 如果一个类没有继承任何类，则默认继承object
# 定义子类时，必须在其构造函数中调用父类的构造函数
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('姓名：{0}，年龄：{1}'.format(self.name,self.age))

class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score=score

class Teacher(Person):
    def __init__(self,name,age,teacheryear):
        super().__init__(name,age)
        self.teacheryear=teacheryear

stu=Student('张三',20,100)
stu.info()
print(stu.score)

tea=Teacher('李四',50,28)
tea.info()
print(tea.teacheryear)