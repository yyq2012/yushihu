# \_\_slots\_\_魔法

# 我们讲到这里，不知道大家是否已经意识到，
# Python是一门[动态语言](https://zh.wikipedia.org/wiki/%E5%8A%A8%E6%80%81%E8%AF%AD%E8%A8%80)。
# 通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，
# 当然也可以对已经绑定的属性和方法进行解绑定。
# 但是如果我们需要限定自定义类型的对象只能绑定某些属性，
# 可以通过在类中定义\_\_slots\_\_变量来进行限定。
# 需要注意的是\_\_slots\_\_的限定只对当前类的对象生效，
# 对子类并不起任何作用。

class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

    # def __str__(self):
    #     return '$s, %s, %s' % (str(self._name), str(self._age), )
def main():
    person = Person("张三", 23)
    person.play()
    person._gender = '男'
    print(person)


if __name__ == '__main__':
    main()
