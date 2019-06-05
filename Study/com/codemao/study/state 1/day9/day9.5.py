#  类之间的关系
#
# 简单的说，类和类之间的关系有三种：is-a、has-a和use-a关系。
#
# - is-a关系也叫继承或泛化，比如学生和人的关系、手机和电子产品的关系都属于继承关系。
# - has-a关系通常称之为关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系；
#   关联关系如果是整体和部分的关联，那么我们称之为聚合关系；
#   如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），
#   那么这种就是最强的关联关系，我们称之为合成关系。
# - use-a关系通常称之为依赖，比如司机有一个驾驶的行为（方法），
#   其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系。
#
#
# 利用类之间的这些关系，我们可以在已有类的基础上来完成某些操作，
# 也可以在已有类的基础上创建新的类，这些都是实现代码复用的重要手段。
# 复用现有的代码不仅可以减少开发的工作量，也有利于代码的管理和维护，
# 这是我们在日常工作中都会使用到的技术手段。


# 继承和多态

# 刚才我们提到了，可以在已有类的基础上创建新类，
# 这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，
# 从而减少重复代码的编写。提供继承信息的我们称之为父类，也叫超类或基类；
# 得到继承信息的我们称之为子类，也叫派生类或衍生类。
# 子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，
# 所以子类比父类拥有的更多的能力，
# 在实际开发中，我们经常会用子类对象去替换掉一个父类对象，
# 这是面向对象编程中一个常见的行为

class Person(object):
    """人"""

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
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看大片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)


class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('于是乎', 38, '老叫兽')
    t.teach('Python程序设计')
    t.watch_av()


if __name__ == '__main__':
    main()