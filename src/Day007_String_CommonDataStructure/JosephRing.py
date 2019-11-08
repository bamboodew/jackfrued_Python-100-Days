import time
from random import sample


def main():
    persons = [x for x in range(1, 31)]
    # print(persons)
    notChristians = []
    while len(persons) > 15:
        notChristians += [persons[8]]
        persons = persons[9:] + persons[:8]
        print(persons)
        # print(persons)
    notChristians.sort()
    persons.sort()
    print('非基督徒位置:', notChristians)
    print('基督徒的位置:', persons)
    print()


if __name__ == '__main__':
    main()
