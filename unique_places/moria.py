#!/usr/bin/python

import random

import constants
from battle_engine import battle
from items.armor import Armor
from items.item import Item
from items.weapon import Weapon
from unique_place import UniquePlace


class Moria(UniquePlace):
    """
    墨瑞亚是迷雾山脉南部中的独特地点。在托尔金的宇宙中，墨瑞亚是一个巨大的地下城市，由矮人建造，现在已被奥克占领。
    
    如果玩家访问墨瑞亚，他在墨瑞亚花费的时间将是一个随机生成的值，在15-25回合之间。
    在每个回合中，玩家都有机会遇到一群奥克。每一次遭遇都会增加未来遭遇的概率，直到玩家需要不断地从奥克手中逃跑。

    这是如何工作的：
    -有三种“旅行”方式：低风险旅行、中风险旅行和高风险旅行。调用哪个方法取决于self._danger。
    -如果玩家遇到怪物，self._danger加一。
    -三种旅行方式中的每一种都有自己的PDF，用于确定玩家是否遇到怪物。
    
    补充说明：
    -玩家有机会在墨瑞亚遇到炎魔。炎魔是一个非常强大的怪物，玩家应该逃离它。
    -玩家在穿越墨瑞亚时有机会拾取物品。
    """

    def __init__(self, name, description, greetings):
        """
        初始化墨瑞亚。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)

        # 低风险活动的字符串
        self._sneakString = ["你继续穿过狭窄的大厅，试图避免被发现......",
                             "你匍匐过一个腐烂的图书馆......",
                             "你匍匐在矿井中....",
                             "你偷偷穿过一些古老的隧道......",
                             "你爬过迷宫般的机械群......",
                             "你偷偷溜过一连串的尸体......",
                             "你偷偷溜过一些奇怪的石碑......"]

        # 中风险活动的字符串
        self._neutralString = ["你发现楼梯上堆满了矮人战士的尸体。",
                               "你经过一个巨大的矿井。",
                               "你似乎迷路了，然后转身回去。",
                               "你发现自己在一个巨大的大厅里，尽头是一个蜿蜒的楼梯。",
                               "你路过曾经是聚会场所的地方。",
                               "你藉由相信自己的直觉，转了一系列的弯。",
                               "你发现自己被困住了，必须转身回去。"]

        # 遭遇战斗的字符串
        self._encounterString = ["你听到一些脚步声......",
                                 "你觉得自己看到一些影子在移动......",
                                 "你听到一连串激动的咕哝声....",
                                 "你看到影子在远处飞快地移动....",
                                 "你听到黑暗中的低语...."]

        # 如果玩家正在躲避怪物，则为字符串
        self._runString = ["你从一些腐烂的尸体上跑过！",
                           "你跑过一个螺旋楼梯！",
                           "你沿着一些矿车飞奔！",
                           "你沿着圆柱大厅冲刺！",
                           "你沿着一个大矿井冲刺！",
                           "你飞快地跑过一些古墓！",
                           "你爬过了一堆瓦砾！"]

        # 生成战利品
        description = "取自一个被杀的矮人战士"
        weapon = Weapon("生锈的斧头", description, 6, 8, 12)
        description = "矮人工匠用过的锤子"
        weapon2 = Weapon("矮人锤", description, 10, 12, 16)
        description = "沉浸在历史中"
        weapon3 = Weapon("艾文", description, 8, 22, 18)
        description = "具有历史意义"
        weapon4 = Weapon("杜恩海姆", description, 4, 18, 3)
        description = "老旧但仍然有效"
        armor = Armor("铁帽", description, 3, 4, 1)
        description = "可能会增加魔力知觉"
        armor2 = Armor("旅行之靴", description, 2, 8, 2)
        description = "中洲最稀有的金属之一"
        item = Item("秘银", description, 0, 84)
        description = "神奇的性质？"
        item2 = Item("古代符文", description, 2, 42)
        self._loot = [weapon, weapon2, weapon3, weapon4, armor, armor2, item, item2]

    def enter(self, player):
        """
        来到都林之门。

        @param player:   玩家对象
        """
        # 剧情
        print("\n你来到了墨瑞亚的西墙前。")
        input("按回车键继续。")
        print("")

        print("经过一番仔细的查找，你在石壁上发现这行淡淡的铭文：")
        print("'墨瑞亚之主，都林之门。请说，朋友，然后进入。'")
        input("按回车键继续。")
        print("")

        # 征求用户输入
        acceptable = ["friend", "leave"]
        while True:
            choice = input("请输入开门密语(英文的)或者离开(leave)：")
            if choice in acceptable:
                break
            else:
                damage = player.takeAttack(constants.WATCHER_IN_THE_WATER_ATTACK)
                print("\n水中监视者从湖里伸出的强壮触手对 %s 造成 %s 点伤害！" % (player.getName(), damage))
                if not player.getHp():
                    print("千钧一发之际！甘道夫把你救了出来...")
                    player.heal(1)
                    player.reduceExperience()
                    return
        print("")

        # 成功开启都林之门或者离开
        if choice == "friend":
            print("伴随着咔嚓一声闷响，都林之门从中间向外打开了。")
            if not player.canMoveEast():
                self._createPort("east")
        else:
            print("你实在摸不着头脑，只能悻悻而回。")

    def through(self, player):
        """
        通过墨瑞亚的动作序列。
        
        @param player:   玩家对象

        @return:         如果成功通过则为True，否则为False
        """
        # 剧情
        print(self._greetings)
        print("")

        print("你进入一个曾经辉煌的大厅，在阴影中快速移动。")
        input("按回车键继续。")
        print("")

        # 危险跟踪器
        self._danger = 0

        # 生成在墨瑞亚度过的时间长度
        timeInMoria = random.randrange(15, 25)

        # 玩家穿越墨瑞亚的旅程
        for time in range(timeInMoria):
            if self._danger < constants.MORIA_LOW_RISK_UPPER_LIMIT:
                result = self._lowRiskTravel(player)
            elif self._danger < constants.MORIA_MED_RISK_UPPER_LIMIT:
                result = self._mediumRiskTravel(player)
            else:
                result = self._highRiskTravel(player)

            # 执行动作序列
            print(result[0])
            print("")
            input("按回车键继续。")
            print("")

            if result[1]:
                result = battle(player, constants.BattleEngineContext.RANDOM)
                if not result:
                    return False

        # 结束序列
        print("你从墨瑞亚矿坑中出来了!")
        input("按回车键继续。")
        print("")
        return True

    def _lowRiskTravel(self, player):
        """
        决定玩家在墨瑞亚矿坑进行低风险旅行的结果。
        
        @param player:  玩家对象
        """
        chance = random.random()
        if chance < constants.MORIA_LOW_RISK_SNEAK_UPPER_LIMIT:
            statement = random.choice(self._sneakString)
            battle = False
            self._itemFind(player)
        elif chance < constants.MORIA_LOW_RISK_NEUTRAL_UPPER_LIMIT:
            statement = random.choice(self._neutralString)
            battle = False
            self._itemFind(player)
        else:
            statement = random.choice(self._encounterString)
            self._danger += 1
            battle = True

        return statement, battle

    def _mediumRiskTravel(self, player):
        """
        决定玩家在墨瑞亚矿坑进行中风险旅行的结果。
        
        @param player:  玩家对象
        """
        chance = random.random()
        if chance < constants.MORIA_MED_RISK_SNEAK_UPPER_LIMIT:
            statement = random.choice(self._sneakString)
            battle = False
            self._itemFind(player)
        elif chance < constants.MORIA_MED_RISK_NEUTRAL_UPPER_LIMIT:
            statement = random.choice(self._neutralString)
            battle = False
            self._itemFind(player)
        else:
            statement = random.choice(self._encounterString)
            self._danger += 1
            battle = True

        return statement, battle

    def _highRiskTravel(self, player):
        """
        决定玩家在墨瑞亚矿坑进行高风险旅行的结果。
        
        @param player:  玩家对象
        """
        chance = random.random()
        if chance < constants.MORIA_HIGH_RISK_NEUTRAL_UPPER_LIMIT:
            statement = random.choice(self._neutralString)
            battle = False
            self._itemFind(player)
        else:
            statement = random.choice(self._runString)
            self._danger += 1
            battle = True

        return statement, battle

    def _itemFind(self, player):
        """
        决定玩家是否找到一个物品以及什么物品。
        
        @param player:  玩家对象
        """
        chance = random.random()
        if self._loot and chance < constants.MORIA_ITEM_FIND_PROB:
            item = random.choice(self._loot)
            print("你在穿越墨瑞亚矿坑时发现了 %s ！" % item.getName())

            if player.addToInventory(item):
                self._loot.remove(item)

            input("按回车键继续。")
            print("")
