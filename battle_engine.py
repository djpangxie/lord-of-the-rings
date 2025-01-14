#!/usr/bin/python

import math
import random

import constants
import factories.monster_factory
from commands.use_potion_command import UsePotionCommand
from items.unique_items import eliteLevelFindableUniques
from items.unique_items import highLevelFindableUniques
from items.unique_items import lowLevelFindableUniques
from util.helpers import triangular


def battle(player, context, monsters=None):
    """
    指环王的战斗引擎。

    @param player:     玩家对象
    @param context:    战斗引擎的模式，战斗引擎在不同模式下有不同的表现
                       战斗要么是随机战斗，要么是基于故事的战斗（例如：BOSS战）
    @param monsters:   用于基于故事的战斗的可选参数，包含要战斗的怪物列表
                       
    @return:           如果战斗获胜则为True；否则为False

    随机战斗和剧情战斗的区别：
    -随机战斗：调用monster_factory模块中的getMonsters()函数来生成怪物。玩家可以在随机战斗中成功奔跑。
    -剧情战斗：怪物必须通过monsters参数提供。玩家不能从剧情战斗中逃跑。
    """
    # 战斗设置
    output = _battleSetup(player, context, monsters)
    if context == constants.BattleEngineContext.RANDOM:
        bonusDifficulty = output[0]
        monsters = output[1]
        # 如果没有生成怪物
        if len(monsters) == 0:
            return
    else:
        bonusDifficulty = output

    quick = False
    earnings = [0, 0]
    acceptable = ["quick", "attack", "use", "run"]

    # 主要的战斗过程
    while monsters:
        # 显示敌方怪物
        print("敌人：")
        for num, monster in enumerate(monsters, 1):
            print("\t%d.%-20s%s" % (num, monster.getName(), monster.getDescription()))
        print("")

        # 用户输入行动选项
        if quick:
            num = 1
            choice = "attack"
        else:
            num = -1
            choice = None

        while choice not in acceptable:
            choice = input("你可以：快进(quick)、进攻(attack)、道具(use)、撤退(run)> ")
            try:
                choice, num = choice.split(' ', 2)
                num = int(num)
            except ValueError:
                num = -1

        # 玩家攻击选项
        if choice == 'attack':
            earnings = _playerAttackPhase(player, monsters, bonusDifficulty, earnings, num)

        # 使用物品选项
        elif choice == "use":
            _usePotion(player)

        # 玩家撤退选项
        elif choice == "run":
            if context == constants.BattleEngineContext.RANDOM:
                if random.random() > constants.BattleEngine.RUN_PROBABILITY_SUCCESS * (1 + bonusDifficulty):
                    print("你成功摆脱了敌人的追踪！")
                    print("")
                    return False
                else:
                    print("你被敌人追上了！")
            else:
                print("你撤退的路被堵死了！")

        # 快进 - 玩家依次按顺序砍倒敌人直到被敌人砍倒或获得胜利
        elif choice == "quick":
            quick = True
            earnings = _playerAttackPhase(player, monsters, bonusDifficulty, earnings, 1)

        # 在玩家阶段和怪物阶段之间等待
        if not quick:
            input("按回车键继续。")
        print("")

        # 怪物攻击阶段
        continueBattle = _monsterAttackPhase(player, monsters)

        # 如果战斗失败的话
        if not continueBattle:
            print("")
            print("甘道夫把你救了出来...")
            player.heal(1)
            player.reduceExperience()
            return False

    # 战斗结束 - 获得战利品
    _endSequence(player, earnings)

    return True


def _battleSetup(player, context, monsters):
    """
    为战斗引擎生成变量并打印战斗启动画面。
    """
    # 对于随机战斗
    if context == constants.BattleEngineContext.RANDOM:
        # 创建变量
        location = player.getLocation()
        region = location.getRegion()
        bonusDifficulty = location.getBattleBonusDifficulty()

        # 生成怪物
        monsterCount = _monsterNumGen(player)
        monsters = factories.monster_factory.getMonsters(monsterCount, region, bonusDifficulty)

        # 宣战信息
        print("遭遇到随机战斗！")
        print("")

        return bonusDifficulty, monsters

    # 对于剧情战斗
    elif context == constants.BattleEngineContext.STORY:
        # 创建变量
        location = player.getLocation()
        region = location.getRegion()
        bonusDifficulty = location.getBattleBonusDifficulty()

        # 为剧情怪物补满生命值
        for monster in monsters:
            monster.recoverHp()

        # 剧情头幕
        print("""
()==[:::::::::::::> ()==[:::::::::::::> ()==[:::::::::::::>
""")
        return bonusDifficulty

    else:
        errorMsg = "传给_battleSetup()函数的战斗模式参数无效。"
        raise AssertionError(errorMsg)


def _monsterNumGen(player):
    """
    辅助函数，用于确定生成的怪物数量。
    
    首先是地区的基础怪物生成数量，然后算上该地区的难度加成，最后使用正态分布来制造波动。
    
    @param player:     玩家对象

    @return:           怪物数量的整数值
    """
    location = player.getLocation()
    region = location.getRegion()
    bonusDifficulty = location.getBattleBonusDifficulty()

    # 计算区域生成量
    if region == constants.RegionType.ERIADOR:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.ERIADOR
    elif region == constants.RegionType.BARROW_DOWNS:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.BARROW_DOWNS
    elif region == constants.RegionType.HIGH_PASS:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.HIGH_PASS
    elif region == constants.RegionType.ENEDWAITH:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.ENEDWAITH
    elif region == constants.RegionType.MORIA:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.MORIA
    elif region == constants.RegionType.RHOVANION:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.RHOVANION
    elif region == constants.RegionType.ROHAN:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.ROHAN
    elif region == constants.RegionType.GONDOR:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.GONDOR
    elif region == constants.RegionType.MORDOR:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.MORDOR
    else:
        errorMsg = "地区类型无效：找不到该地区类型。"
        raise AssertionError(errorMsg)

    # 使用正态分布来制造波动
    standardDeviation = monsterCount / constants.BattleEngine.STANDARD_DEVIATION

    monsterCount = random.normalvariate(monsterCount, standardDeviation)
    monsterCount = max(math.floor(monsterCount), 1)
    monsterCount = int(monsterCount)

    return monsterCount


def _playerAttackPhase(player, monsters, bonusDifficulty, earnings, num):
    """
    当用户开始攻击单个怪物对象时，如果怪物的生命值降至零，则将怪物从战斗中移除。

    此外，经验和金钱是根据奖金计算的。

    @param player:           玩家对象
    @param monsters:         怪物对象列表
    @param bonusDifficulty   当前地区的难度加成
    @param earnings:         两个元素的列表，第一个是获得的金钱，第二个是获得的经验
                             这两个值整场战斗中都会在函数间传递，并将积累所有的收益
    @param num:              一开始就传入的怪物序号
    
    @return:                 同上述的earnings参数引向的列表的中两个元素，第一个是获得的金钱，第二个是获得的经验
    """
    # 开始战斗收益
    money = earnings[0]
    experience = earnings[1]

    while True:
        # 输入攻击目标
        if num == -1:
            try:
                target = input("输入怪物的整数序号值：")
                target = int(target)
            except ValueError:
                target = -1
        else:
            target = num
            num = -1
        print("")

        if 1 <= target <= len(monsters):
            # 进行攻击
            print("%s 对 %d.%s 造成了 %s 点伤害！" % (
                player.getName(), target, monsters[target - 1].getName(), player.attack(monsters[target - 1])))
            # 如果怪物还活着
            if monsters[target - 1].getHp() > 0:
                print("%d.%s 还剩 %s 点生命值。" % (target, monsters[target - 1].getName(), monsters[target - 1].getHp()))
            # 如果怪物死了
            else:
                print("%s" % monsters[target - 1].getDeathString())
                # 从赢得战斗中获得收益
                expIncrease = monsters[target - 1].getExperience() * (1 + bonusDifficulty)
                experience += math.floor(expIncrease)
                money += math.floor(expIncrease / constants.BattleEngine.MONEY_CONSTANT)
                # 从怪物列表中移除怪物
                monsters.pop(target - 1)
            break
        else:
            print("怪物序号输入有误！")

    return money, experience


def _usePotion(player):
    """
    创建一个特殊的UsePotionCommand命令对象（仅用于战斗中），然后执行其execute()方法。

    @param player:   玩家对象
    """
    # 这里不该使用喝药的命令，等会应该修改成在战斗中使用物品的函数
    usePotionCmd = UsePotionCommand(" ", " ", player)
    usePotionCmd.execute()


def _monsterAttackPhase(player, monsters):
    """
    怪物攻击阶段 - 当怪物攻击玩家时。

    @param player:      玩家对象
    @param monsters:    怪物对象的列表

    @return:            如果将要继续战斗则为True，否则为False
    """
    # 怪物攻击
    for num, monster in enumerate(monsters, 1):
        print("%d.%s *%s* 并对 %s 造成 %s 点伤害！" % (
            num, monster.getName(), monster.getAttackString(), player.getName(), monster.attack(player)))

        # 玩家挂了
        if not player.getHp():
            print("\n%d.%s 击败了 %s " % (num, monster.getName(), player.getName()))
            return False

    print("\n%s 还剩 %s 点生命值。\n" % (player.getName(), player.getHp()))

    # 战斗继续
    return True


def _itemFind(player, experience):
    """
    计算玩家是否获取物品以及获取哪件物品。
    
    @param player:         玩家对象
    @param experience:     从战斗中获得的经验值
    """
    location = player.getLocation()

    # 有可能获取独特物品
    lowLevel = triangular(constants.ItemFind.lowLevel)
    if experience > lowLevel and lowLevelFindableUniques:
        item = random.choice(lowLevelFindableUniques)
        print("你找到了 %s ！" % item.getName())
        if not player.addToInventory(item):
            location.addItem(item)

    # 有可能获取精英级独特物品
    highLevel = triangular(constants.ItemFind.highLevel)
    if experience > highLevel and highLevelFindableUniques:
        item = random.choice(highLevelFindableUniques)
        print("你找到了 %s ！" % item.getName())
        if not player.addToInventory(item):
            location.addItem(item)

    # 有可能获取精英级独特宝物
    eliteLevel = triangular(constants.ItemFind.eliteLevel)
    if experience > eliteLevel and eliteLevelFindableUniques:
        item = random.choice(eliteLevelFindableUniques)
        print("你找到了 %s ！" % item.getName())
        if not player.addToInventory(item):
            location.addItem(item)


def _endSequence(player, earnings):
    """
    战斗胜利后的扫尾工作：
    -显示胜利信息。
    -可能找到独特物品。
    -增加角色的经验和金钱。

    @param player:      玩家对象
    @param earnings:    两个元素的列表，第一个是获得的金钱，第二个是获得的经验
    """
    money = earnings[0]
    experience = earnings[1]

    victoryDeclaration = "敌人被消灭了！"
    gainsDeclaration = "%s 总共获得 %s 金钱，以及 %s 经验值！" % (player.getName(), money, experience)

    lengthBar = len(gainsDeclaration)
    victoryDeclaration = victoryDeclaration.center(lengthBar)
    bar = "——" * lengthBar

    print(bar)
    print(victoryDeclaration)
    print(gainsDeclaration)
    _itemFind(player, experience)
    player.increaseMoney(money)
    player.increaseExperience(experience)
    print(bar)
    print("")
