import time


def main():
    # 通过for循环逐行读取
    with open('致橡树.txt', encoding='UTF-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()


if __name__ == '__main__':
    main()
