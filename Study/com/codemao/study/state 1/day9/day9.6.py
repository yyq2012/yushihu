# 子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，
# 这个动作称之为方法重写（override）。
# 通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，
# 当我们调用这个经过子类重写的方法时，
# 不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪!!!' % self._nickname)


class Cat(Pet):
    '''猫'''

    def make_voice(self):
        print('%s: 喵喵喵!!!' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


if __name__ == '__main__':
    main()


# 在上面的代码中，我们将`Pet`类处理成了一个抽象类，
# 所谓抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。
# Python从语法层面并没有像Java或C#那样提供对抽象类的支持，
# 但是我们可以通过`abc`模块的`ABCMeta`元类和`abstractmethod`包装器来达到抽象类的效果，
# 如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）。
# 上面的代码中，`Dog`和`Cat`两个子类分别对`Pet`类中的`make_voice`抽象方法进行了重写并给出了不同的实现版本，
# 当我们在`main`函数中调用该方法时，
# 这个方法就表现出了多态行为（同样的方法做了不同的事情）。

