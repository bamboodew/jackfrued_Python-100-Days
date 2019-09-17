from abc import abstractmethod, ABCMeta
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):
    """战斗者"""
    # 通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name', '_hp')  # hp代表生命值

    def __init__(self, name, hp):
        """初始化
        :param name:名字
        :param hp:生命值
        """
        self._name = name
        self._hp = hp

    @property  # getter
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0  # 血量>0就是活着的

    @abstractmethod
    def attack(self, other):
        """
        攻击
        :param other:被攻击的对象
        """
        pass


class Ultraman(Fighter):
    """奥特曼"""
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """初始化
        :param name:名字
        :param hp:生命值
        :param mp:魔法值
        """
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)  # 攻击一次，怪兽的血量随机减少15~25

    def huge_attack(self, other):
        """
        大招/终极必杀技：打掉怪兽max(50点,3/4的血量)
        :param other:被攻击的对象
        :return:使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50  # 自身魔法值减掉50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury  # 怪兽生命值减掉50或3/4
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, other):
        """
        魔法攻击
        :param other:被攻击的对象
        :return:使用魔法成功返回True否则返回False
        """

    def resume(self):
        """
        恢复魔法值
        :return:
        """
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
               '生命值：%d\n' % self._hp + \
               '魔法值：%d\n' % self._mp


class Monster(Fighter):
    """怪兽"""
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)  # 被怪兽攻击掉血10~20点

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
               '生命值：%d\n' % self._hp


def is_any_alive(monsters):
    """判断有没有小怪兽是活着的"""
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    """选中一只活着的小怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    # 设定奥特曼的属性：名字、生命值hp、魔法值mp
    ultraman = Ultraman('Luo', 1000, 120)
    # 设定怪兽1的属性：名字、生命值hp
    monster1 = Monster('Di', 250)
    # 设定怪兽2的属性：名字、生命值hp
    monster2 = Monster('Bai', 500)
    # 设定怪兽3的属性：名字、生命值hp
    monster3 = Monster('Wang', 750)
    # 成立怪兽组
    monsters = [monster1, monster2, monster3]
    # 第一回合开始
    fight_round = 1
    # 只要奥特曼和怪兽还活着，就一直战斗
    while ultraman.alive and is_any_alive(monsters):
        print('========第%02d回合========' % fight_round)
        # 随机选择一个活着的小怪兽
        monster = select_alive_one(monsters)
        # 随机选择奥特曼的技能
        skill = randint(1, 10)  # 通过随机数选择使用技能
        # 60%的概率
        if skill <= 6:
            print('%s使用普通攻击打了%s.' % (ultraman.name, monster.name))
            # 使用普通攻击
            ultraman.attack(monster)
            # 随机恢复1~9点魔法值
            print('%s的魔法值恢复了%d点.' % (ultraman.name, ultraman.resume()))

        # 30%的概率
        elif skill <= 9:
            # 如果魔法足够
            if ultraman.magic_attack(monster):
                # 使用魔法攻击
                print('%s使用了魔法攻击.' % ultraman.name)
            # 可能因魔法值不足
            else:
                # 失败
                print('%s使用魔法失败.' % ultraman.name)

        # 10%的概率
        else:
            # 魔法足够，使用究极必杀技
            if ultraman.huge_attack(monster):
                print('%s使用究极必杀技虐了%s.' % (ultraman.name, monster.name))
            # 魔法不足，
            else:
                # 如果魔法值不足
                print('%s使用普通攻击打了%s.' % (ultraman.name, monster.name))
                # 使用普通攻击
                ultraman.attack(monster)
                print('%s的魔法值恢复了%d点.' % (ultraman.name, ultraman.resume()))
        # 如果怪兽还活着
        if monster.alive > 0:
            # 怪兽就回击奥特曼
            print('%s回击了%s.' % (monster.name, ultraman.name))
            monster.attack(ultraman)
        # 显示奥特曼和怪兽的属性
        display_info(ultraman, monsters)
        # 增加一个回合
        fight_round += 1

    print('\n========战斗结束========\n')
    if ultraman.alive > 0:
        print('%s奥特曼胜利！' % ultraman.name)
    else:
        print('小怪兽胜利！')


if __name__ == '__main__':
    main()
