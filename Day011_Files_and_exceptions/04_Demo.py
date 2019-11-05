import time


def main():
    # 读取文件按行读取到列表中
    with open('致橡树.txt', encoding='UTF-8') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
