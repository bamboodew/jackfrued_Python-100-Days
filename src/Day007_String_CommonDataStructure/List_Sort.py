def main():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)  # 按首字母排序
    print('list2: %s' % list2)

    list1.sort(reverse=True)
    print('list1: %s' % list1)    # 按首字母反向排序

    list3 = sorted(list1, reverse=True)  # 逆序
    print('list3: %s' % list3)

    list4 = sorted(list1, key=len)
    print('list4: %s' % list4)
    list4.reverse()    # 直接反向排序
    print('list1: %s' % list4)


if __name__ == '__main__':
    main()
