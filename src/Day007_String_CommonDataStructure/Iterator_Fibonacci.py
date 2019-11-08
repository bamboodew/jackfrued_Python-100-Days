def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a  # 生成器


def main():
    i = int(input('请输入：'))
    for val in fib(i):
        print(val, end=' ')


if __name__ == '__main__':
    print(fib(10))  # <generator object fib at 0x0115AB70>
    print(next(fib(10)))  # 10
    main()
