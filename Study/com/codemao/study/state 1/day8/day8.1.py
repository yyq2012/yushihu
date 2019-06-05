# 定义类
# 在Python中可以使用`class`关键字定义类，然后在类中通过之前学习过的函数来定义方法，
# 这样就可以将对象的动态特征描述出来，代码如下所示。

class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_tv(self):
        if self.age < 18:
            print('%s只能看<<熊出没>>.' % self.name)
        else:
            print('%s可以看编程课.' % self.name)
    # **说明**：写在类中的函数，我们通常称之为（对象的）方法，这些方法就是对象可以接收的消息。


# 创建和使用对象
# 当我们定义好一个类之后，可以通过下面的方式来创建对象并给对象发消息。

def main():
    # 创建学生对象并制定姓名和年龄
    student1 = Student('张三', 12)
    student2 = Student('李四', 28)

    # 给对象发study消息
    student1.study('小学数学')
    student2.study('线性代数')
    # 给对象发watch_tv消息
    student1.watch_tv()
    student2.watch_tv()


if __name__ == '__main__':
    main()
