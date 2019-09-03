"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""


def twoSum(nums, target):
    # set0 = set(nums)  # 将数组转换成集合，确保元素不重复；但是将顺序改变了
    # list0 = list(nums)
    tuple0 = []
    list0 = nums
    # return set0
    for i in range(0, len(nums) - 1):
        a = nums[i]
        # set0 = set0.pop()
        # if i + 1 < len(nums):
        list0.remove(list0[0])
        # print(list0)
        for j in range(i + 1, len(nums)):
            b = nums[j]
            if a + b == target & a not in list0:
                tuple0 += [i, j]  # return之后就停止函数的循环
            else:
                break
    return tuple0


def main():
    list0 = [1, 1, 6, 2, 1, 5, 3, 3, 4, 5, 4]
    list1 = [1, 1, 2, 1, 3, 3, 4, 5, 4]
    # print(list0[2:])
    # while 1 in list1:
    #     list1.remove(1)
    # print(list1)
    set1 = set(list0)
    list2 = list(set1)
    list2.sort(key=list0.index)
    print(set1)
    print(list2)

    # 剔除重复元素
    j = 1
    for i in list0[:len(list0) - 1]:
        if i in list1[j:]:
            list1.remove(i)
            # print(list1)
        else:
            j += 1
    print(list1)
    print(set(list1))

    sum1 = lambda arg1, arg2: arg1 ** arg2
    print(sum1(20, 3))


if __name__ == '__main__':
    main()
