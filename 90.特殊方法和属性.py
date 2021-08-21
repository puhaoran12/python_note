#特殊属性__dict__:获得类对象或实例对象所绑定的所有属性和方法
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age

print(C('张三',20).__dict__)
print(C.__dict__)
# 特殊方法
# 1.__len__() 通过重写__len__()方法，让内置函数len()的参数可以是自定义类型
# 2.__add__() 通过重写__add__()方法，可以使用自定义对象具有“+”功能
# 3.__new__() 用于创建对象
# 4.__init__() 对创建的对象进行初始化
class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象的id值为{0}'.format(id(obj)))
        return obj
    def __init__(self,name,age):
        print('__init__被调用执行了，self的id值为{0}'.format(id(self)))
        self.name=name
        self.age=age

print('object这个类对象的id为：{0}'.format(id(object)))
print('Person这个类对象的id为：{0}'.format(id(Person)))

p1=Person('张三',20)
print('p1这个类对象的id为：{0}'.format(id(p1)))
