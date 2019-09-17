# **jackfrued_Python-100-Days**

* ## Day001_FirstPython
* ## Day002_ProgramElements
* ## Day003_BranchStructure
* ## Day004_CircularStructure
* ## Day005_ConstructProgramLogic
* ## Day006_FunctionsAndModules
* ## Day007_String_CommonDataStructure

### 1、2019年9月5~7日：生成9*9数独表

1.1 行内不重复

1.2 列内不重复

1.3 宫内不重复

1.4 第5、7行要保证有可选数，例如：
如下第5行的✖的位置无可选数

❶■■■■■■■■

❷■■■■■■■■

❸■■■■■■■■

❹❺❻■■■■■■

❼❽❾■■■■■■

✖

1.5 第8行直接通过减法得出


### 2、函数和方法

2.1 void——纯动作后台处理；不返回值

2.2 其他——返回值



### 设定奥特曼的属性：名字、生命值hp、魔法值mp
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
