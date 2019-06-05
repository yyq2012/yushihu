# while循环

# 如果要构造不知道具体循环次数的循环结构，我们推荐使用`while`循环，
# `while`循环通过一个能够产生或转换出`bool`值的表达式来控制循环，
# 表达式的值为`True`循环继续，表达式的值为`False`循环结束。
# 下面我们通过一个“猜数字”的小游戏
# （计算机出一个1~100之间的随机数，人输入自己猜的数字，
# 计算机给出对应的提示信息，直到人猜出计算机出的数字）
# 来看看如何使用`while`循环。

# 猜数字游戏
import random

num = random.randint(1, 100)
# print(num)
count = 0
print('来,让我们测测你的智商,我这里出一个1-100的数字,看你几次可以猜中~~')
while True:
    count += 1
    answer = int(input('请输入你的答案:'))
    if "" != answer and None != answer:
        if answer < num:
            print('大一点')
        elif answer > num:
            print('小一点')
        else:
            print('正确答案: %d 您的回答次数: %d' % (num, count))
            break
    else:
        print('请输入一个数字!')
if count > 7:
    print("您的智商余额不足,请充值~~~")
elif count > 5:
    print('您的智商正常,请继续使用!!!')
else:
    print('您的智商超纲,请多多使用!!!')

# 说明：**上面的代码中使用了`break`关键字来提前终止循环，
# 需要注意的是`break`只能终止它所在的那个循环，
# 这一点在使用嵌套的循环结构（下面会讲到）需要引起注意。
# 除了`break`之外，还有另一个关键字是`continue`，
# 它可以用来放弃本次循环后续的代码直接让循环进入下一轮。
# 
# 和分支结构一样，循环结构也是可以嵌套的，也就是说在循环中还可以构造循环结构。
