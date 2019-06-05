# 从上面的例子可以看出，如果程序中的代码只能按顺序一点点的往下执行，
# 那么即使执行两个毫不相关的下载任务，
# 也需要先等待一个文件下载完成后才能开始下一个下载任务，
# 很显然这并不合理也没有效率。

# 接下来我们使用多进程的方式将两个下载任务放到不同的进程中，
# 代码如下所示。
from multiprocessing import Process
from os import getpid
from random import randint
from time import sleep, time


def download_task(filename):
    print('%s进程开始下载...' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s文件下载完成,消耗%.2f秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院', ))
    p1.start()
    # p2 = Process(target=download_tast('从删库到跑路'))
    p2 = Process(target=download_task, args=('从删库到跑路', ))
    p2.start()

    p1.join()
    p2.join()
    end = time()
    print('下载完成,共耗时 %.2f 秒' % (end - start))


if __name__ == '__main__':
    main()


# 在上面的代码中，我们通过`Process`类创建了进程对象，
# 通过`target`参数我们传入一个函数来表示进程启动后要执行的代码，
# 后面的`args`是一个元组，它代表了传递给函数的参数
# 。`Process`对象的`start`方法用来启动进程，
# 而`join`方法表示等待进程执行结束。
# 运行上面的代码可以明显发现两个下载任务“同时”启动了，
# 而且程序的执行时间将大大缩短，不再是两个任务的时间总和

