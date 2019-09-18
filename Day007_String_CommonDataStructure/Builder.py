def fib(maxi):
    n, a, b = 0, 0, 1
    while n < maxi:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


def main():
    L = [x * x for x in range(10)]
    print(L)
    g = (x * x for x in range(10))
    print(next(g))

    for i in g:
        print(i, end=' ')

    for i in g:
        print('%d有没有' % i, end=' ')

    f = fib(20)
    print(f)

    for i in f:
        print(i, end=' ')

    print(odd())
    for i in odd():
        print(i)


if __name__ == '__main__':
    main()
