def main():
    str1 = 'hello, world!'

    print(len(str1))

    print(str1.capitalize())  # 首字母大写
    print(str1.upper())  # 全部变大写

    print(str1.find('or'))
    print(str1.find('shit'))

    print(str1.index('or'))
    # print(str1.index('shit'))

    print(str1.startswith('he'))
    print(str1.startswith('He'))
    print(str1.endswith('!'))

    print(str1.center(50, '*'))
    print(str1.rjust(50, '*'))

    str2 = 'abc123456'

    print(str2[2])
    print(str2[2:5])  # slice切片
    print(str2[2:])
    print(str2[2::3])
    print(str2[::-1])
    print(str2[-3:-1])

    print(str2.isdigit())
    print(str2.isalnum())

    str3 = '    jackfrue@126.com  '
    print(str3)
    print(str3.strip())


if __name__ == '__main__':
    main()
