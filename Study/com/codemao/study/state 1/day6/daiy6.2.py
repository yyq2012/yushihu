# 摇色子
from random import randint


def rollDice(n=3):  # 默认3个色子

    total = 0
    # count = 0
    for count in range(n):  # range(n) 产生的序列从0开始,到n-1 ,不包括n
        num = randint(1, 6)  # randint(1,6) 产生的随机数包括 1和 6
        count += 1
        print('第%d次的色子点数为: %d' % (count, num))
        total += num
    return total


result = rollDice(6)
# print('您的总点数为:%d' % result)
# print('您的总点数为:' + str(result))
print('您的总点数为:', result)
