# 局部变量：在函数内定义并且使用的变量，只在函数内部有效，局部变量使用global声明，这个变量就会成为全局变量
# 全局变量：函数体外定义的变量，可作用于函数内外
def fun():
    global age
    age=20
    print(age)

fun()
print(age)