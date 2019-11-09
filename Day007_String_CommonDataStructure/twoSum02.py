"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""


def twoSum(nums, target):
    # list0 = []
    tuple0 = ()
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if target - nums[i] == nums[i + 1:][j]:
                tuple0 += ([i, j + i + 1],)
    return tuple0


def main():
    list1 = [1, 2, 3, 1, 4, 5, 2, 6, 7, 8, 9]
    print(twoSum(list1, 6))
    print(twoSum(list1, 10))


if __name__ == '__main__':
    main()
