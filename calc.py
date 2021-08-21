#91.自定义导入模块
def add(a,b):
    return a+b
def nu(a,b):
    return a-b

if __name__ == '__main__':#只有当运行该程序时输出下面的print，当调用的时候下面的print不输出
    print(add(30,40))