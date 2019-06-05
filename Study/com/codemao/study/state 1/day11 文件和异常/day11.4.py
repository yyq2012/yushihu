# 除了使用文件对象的`read`方法读取文件之外，
# 还可以使用`for-in`循环逐行读取或者
# 用`readlines`方法将文件按行读取到一个列表容器中，
# 代码如下所示。


import time


def main():
    # 一次性读取整个文件内容
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('致橡树.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('致橡树.txt') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()