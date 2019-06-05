# 练习1: 将华氏温度转换为摄氏温度
# F 华氏温度  C 摄氏温度
# 转化方式
# F = 1.8C + 32
#
import math

# f = float(input('请输入华氏温度: '))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# 练习2：输入圆的半径计算计算周长和面积。

# r = int(input('请输入半径: '))
# perimeter = 2 * math.pi * r
# area = math.pi * r ** 2
#
# print('周长:%.2f' % perimeter)
# print('面积:%.2f' % area)

# 练习3：输入年份判断是不是闰年。

year = int(input('请输入年份: '))
is_leap: bool = (year % 4 == 0 and year % 100 == 0 or year % 400 == 0)
print(is_leap)

