"""
知道了如何读写文本文件要读写二进制文件也就很简单了，
下面的代码实现了复制图片文件的功能。
"""


def main():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # output:<class 'bytes'>
        with open('吉多.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError:
        print('指定的文件无法打开.')
    except IOError:
        print('度写文件时出现错误.')
    print('程序执行结束')


if __name__ == '__main__':
    main()
