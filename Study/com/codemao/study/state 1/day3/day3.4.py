# 练习3：输入三条边长如果能构成三角形就计算周长和面积
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print('周长 %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积 %.2f' % area)
else:
    print('不能构成三角形')

# 说明：**上面的代码中使用了`math`模块的`sqrt`函数来计算平方根。
# 用边长计算三角形面积的公式叫做[海伦公式]
