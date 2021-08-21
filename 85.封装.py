#如果类的属性不希望在类的外部使用，可以在属性名前面加__ ,但可以被类的内部使用
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  #年龄不希望在类的外部被使用，所以加了__
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()
print(stu.name)
#__age不能被外部直接使用
#print(stu.__age)#AttributeError: 'Student' object has no attribute '__age'