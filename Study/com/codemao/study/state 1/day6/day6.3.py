# 可变参数
# 具体有多少个参数是由调用者来决定，我们作为函数的设计者对这一点是一无所知的，
# 因此在不确定参数个数的时候，我们可以使用可变参数，代码如下所示

# 在参数名前面的*表示args是一个可变参数

# def add(a=0, b=0, c=0):
#     return a + b + c
#
#
# result = add(1, 2, 3)
# print('结果为:',result)

def add2(*args):
    total = 0
    for val in args:
        total += val
    return total


result = add2()
# result = add2(1, 2, 3, 5, 6, 7, 7, 8, 8, )
print('结果为:', result)
