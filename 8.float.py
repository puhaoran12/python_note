# 浮点类型
# 1.浮点数由整数部分和小数部分组成
# 2.浮点数存储不精确性：使用浮点数进行计算时，可能会出现小数位数不确定的情况
print(1.1+2.2)
#解决方法
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))