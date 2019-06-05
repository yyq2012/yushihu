# 请注意上面的代码，如果`open`函数指定的文件并不存在或者无法打开，
# 那么将引发异常状况导致程序崩溃。为了让代码有一定的健壮性和容错性，
# 我们可以使用Python的异常机制对可能在运行时发生状况的代码进行适当的处理，
# 如下所示。

def main():
    file_path = 'text/firstclass.txt'
    encoding = 'UTF-8'  #GBK
    file = None
    try:
        file = open(file_path,'r', encoding= 'GBK')
        print(file.read())
    except FileNotFoundError:
        print('文件未找到')
    except LookupError:
        print('错误的编码格式')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    finally:
        if file:
            file.close()


if __name__ == '__main__':
    main()

    