#!/usr/bin/python

import random

import constants
from battle_engine import battle
from items.unique_items import phialOfGaladriel
from monsters.orc_archer_ii import OrcArcher_II
from monsters.orc_ii import Orc_II
from monsters.shelob import Shelob
from unique_place import UniquePlace


class TowerOfCirithUngol(UniquePlace):
    """
    奇立斯乌苟之塔是奇立斯乌苟中的独特地点。它是守卫着奇立斯乌苟的堡垒。

    如果玩家进入这里，他可能会与尸罗战斗，再然后可能与堡垒中的怪物战斗。
    """

    def __init__(self, name, description, greetings):
        """
        初始化奇立斯乌苟之塔。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)

        self._wave = []
        self._wave2 = []

        # 创建第一波怪物
        monster = Shelob(constants.MONSTER_STATS[Shelob])
        self._wave.append(monster)

        # 创建第二波怪物
        for monster in range(15):
            monster = Orc_II(constants.MONSTER_STATS[Orc_II])
            self._wave2.append(monster)
        for monster in range(6):
            monster = OrcArcher_II(constants.MONSTER_STATS[OrcArcher_II])
            self._wave2.append(monster)

    def enter(self, player):
        """
        奇立斯乌苟之塔的动作序列。
        
        @param player:   玩家对象
        """
        # 剧情
        print(self._greetings)
        print("")

        print("当你爬上奇立斯乌苟的小径时，你凝视着米那斯魔古尔的恐怖魔窟。")
        input("按回车键继续。")
        print("")

        # 征求用户选择
        choice = self._choice()

        # 用户选择的动作序列
        if choice == "yes":
            self._shelobClef(player)
        else:
            print("你活到了新的一天，可以继续去战斗了。")
            print("")

    def _choice(self):
        """
        确定用户是要攻击还是逃跑。
        """
        # 征求用户选择
        print("要继续前进，你必须先穿过尸罗的巢穴。")
        choice = None
        acceptable = ["yes", "no"]
        while choice not in acceptable:
            choice = input("你想要继续前进吗？选项：是(yes)、否(no) ")
        print("")

        return choice

    def _shelobClef(self, player):
        """
        穿过尸罗的巢穴的动作序列。
        
        @param player:   玩家对象
        """
        # 剧情
        print("当你进入尸罗的巢穴时，你被一种非同寻常的黑暗和腐烂的尸体臭味所包围。")
        input("按回车键继续。")
        print("")

        print("....")
        input("按回车键继续。")
        print("")

        # 如果玩家库存中包含加拉德瑞尔的水晶瓶
        if phialOfGaladriel in player.getInventory():
            print("加拉德瑞尔的水晶瓶照亮了整个洞穴。")
            input("按回车键继续。")
            print("")

            print("光给了你力量......尸罗退却了，它害怕光明。")
            input("按回车键继续。")
            print("")

            # 调用下一个动作序列
            self._cirithUngol(player)
        else:
            # 与尸罗的第一次潜在相遇
            shelobAppearance = random.random()
            if shelobAppearance < constants.CIRITH_UNGOL_SHELOB_PROB:
                result = battle(player, constants.BattleEngineContext.STORY, self._wave.copy())
                if not result:
                    return

            print("你遇到了一张厚厚的蜘蛛网。")
            input("按回车键破坏蛛网。")
            print("")

            # 与尸罗的第二次潜在相遇
            shelobAppearance = random.random()
            if shelobAppearance < constants.CIRITH_UNGOL_SHELOB_PROB:
                result = battle(player, constants.BattleEngineContext.STORY, self._wave.copy())
                if not result:
                    return

            print("....")
            input("按回车键继续。")
            print("")

            # 与尸罗的第三次潜在相遇
            shelobAppearance = random.random()
            if shelobAppearance < constants.CIRITH_UNGOL_SHELOB_PROB:
                result = battle(player, constants.BattleEngineContext.STORY, self._wave.copy())
                if not result:
                    return

            print("你遇到了一张厚厚的蜘蛛网。")
            input("按回车键破坏蛛网。")
            print("")

            # 与尸罗的第四次潜在相遇
            shelobAppearance = random.random()
            if shelobAppearance < constants.CIRITH_UNGOL_SHELOB_PROB:
                result = battle(player, constants.BattleEngineContext.STORY, self._wave.copy())
                if not result:
                    return

            print("....")
            input("按回车键继续。")
            print("")

            # 与尸罗的第五次潜在相遇
            shelobAppearance = random.random()
            if shelobAppearance < constants.CIRITH_UNGOL_SHELOB_PROB:
                result = battle(player, constants.BattleEngineContext.STORY, self._wave.copy())
                if not result:
                    return

            print("你终于从黑暗中走了出来！")
            input("按回车键继续。")
            print("")

            # 调用下一个动作序列
            self._cirithUngol(player)

    def _cirithUngol(self, player):
        """
        奇立斯乌苟之塔的动作序列。
        
        @param player:   玩家对象
        """
        successfulEscape = random.random()
        # 如果玩家成功溜过而未被发现
        if successfulEscape < constants.CIRITH_UNGOL_EVASION_PROB:
            print("你设法潜行并溜过了奇立斯乌苟之塔。")
            input("按回车键继续。")
            print("")
        # 如果玩家被敌人发现
        else:
            print("你试图偷偷溜过奇立斯乌苟之塔，但一队巡逻的奥克发现了你。")
            input("按回车键继续。")
            print("")

            result = battle(player, constants.BattleEngineContext.STORY, self._wave2.copy())
            if not result:
                return

            print("你进入了魔多，但索隆已经知道了你的存在。")
            input("按回车键继续。")
            print("")

        self._space.createExit("east", self._targetSpace, outgoingOnly=True)
        player.moveEast()
        self._space.clearExit("east", True, self._targetSpace)

        space = player.getLocation()
        name = space.getName()
        description = space.getDescription()

        print("你来到了 %s" % name)
        print(description)
