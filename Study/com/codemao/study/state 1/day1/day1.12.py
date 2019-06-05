# 用“from”关键字引入图形化窗口类包tkinter
# 在python3版本中，tkinter一定要小写字母才能正确引入
from tkinter import *

# 注意：在www.codemao.cn官网的在线wood编辑器中，无法加载tkinter库
# 想使用tkinker库，请使用原始Python环境或wood编辑器离线版客户端

# 我们用下面这行代码创造一个窗口
root = Tk()

# 告诉系统，把窗口的标题修改为括号内的文字
root.title("我的第一个python程序")
root.geometry("500x600")
# 创建一个label，并且指定label显示内容“”
# bg=“green”意思是将背景颜色设置为绿色，fg=‘white’意思是将文字颜色设置为白色
label = Label(root, text='hello,world', bg='green', fg='white')
label2 = Label(root, text='goodbye,world', bg='green', fg='white')

# 显示label，必须含有此语句
label.pack()
label2.pack()
# 执行下面代码就可以把窗口展示出来
root.mainloop()
