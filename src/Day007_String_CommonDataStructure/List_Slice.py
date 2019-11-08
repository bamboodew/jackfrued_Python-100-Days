def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']

    for fruit in fruits:
        print(fruit.title(), end=' ')  # 首字母大写
        # print(fruit.capitalize(), end=' ')

    print()

    print(fruits[1:3])
    print(fruits[:0])
    print(fruits[-3:-1])
    print(fruits[::-1])  # 逆向排列


if __name__ == '__main__':
    main()
