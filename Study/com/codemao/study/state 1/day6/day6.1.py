# 函数
# 为了解决重复的问题,把需要重复使用的代码封装到一个模块中,在使用该功能的时候只需要
# 调用该函数就可以了
# 玩球
# def play(ball):
#     print('我会玩:' + ball)
#
#
# play('篮球')
# play('足球')
# play('乒乓球')


# 个人介绍
def introduce(name, age, sex):
    print("我的名字是:%s,我%s岁,我是一个%s生" % (name, age, sex))


name = input('你的姓名: ')
age = input('你的年龄: ')
sex = input('你的性别: ')
introduce(name, age, sex)

# introduce('张三', '12', '男')
# introduce('李四', '8', '女')

# 定义函数

# 在Python中可以使用`def`关键字来定义函数，和变量一样每个函数也有一个响亮的名字，
# 而且命名规则跟变量的命名规则是一致的。在函数名后面的圆括号中可以放置传递给函数的参数，
# 这一点和数学上的函数非常相似，程序中函数的参数就相当于是数学上说的函数的自变量，
# 而函数执行完成后我们可以通过`return`关键字来返回一个值，
# 这相当于数学上说的函数的因变量。

