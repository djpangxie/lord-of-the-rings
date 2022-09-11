#!/usr/bin/python

import random

import constants
from battle_engine import battle
from items.weapon import Weapon
from monsters.goblin import Goblin
from monsters.great_goblin import GreatGoblin
from unique_place import UniquePlace


class GoblinTown(UniquePlace):
    """
    半兽人镇是高隘口中的独特地点。
    
    玩家有机会尝试从半兽人镇周围潜伏过去或直接攻入。
    如果潜伏的尝试不成功，玩家必须同时与大量的怪物作战。
    """

    def __init__(self, name, description, greetings):
        """
        初始化半兽人镇。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)
        self._executed = False  # 通关记录

        # 生成战利品
        weapon1 = Weapon("半兽人砍刀", "对精怪有益，对人类有害", 3, 5, 6)
        weapon2 = Weapon("矮人战斧", "从孤山偷来的", 4, 8, 12)
        weapon3 = Weapon("长柄斧", "看起来是从刚铎人那偷来的赃物", 6, 12, 14)
        self._loot = [weapon1, weapon2, weapon3]

        # 我们将有三波怪物
        self._wave = []
        self._wave2 = []
        self._wave3 = []

        # 创造第一波怪物
        for monster in range(2):
            monster = Goblin(constants.MONSTER_STATS[Goblin])
            self._wave.append(monster)

        # 创造第二波怪物
        for monster in range(8):
            monster = Goblin(constants.MONSTER_STATS[Goblin])
            self._wave2.append(monster)

        # 创造第三波怪物
        for monster in range(4):
            monster = Goblin(constants.MONSTER_STATS[Goblin])
            self._wave3.append(monster)
        monster = GreatGoblin(constants.MONSTER_STATS[GreatGoblin])
        self._wave3.append(monster)

        # 穿过咕噜的洞穴失败时的怪物
        self._wave4 = self._wave + self._wave2 + self._wave3

    def enter(self, player):
        """
        半兽人镇的动作序列。

        @param player:  玩家对象
        """
        print(self._greetings)
        print("")

        # 已经通关了半兽人镇
        if self._executed:
            print("你上次来时已经扫平了这里！")
            input("按回车键继续。")
            print("")
        # 尚未通关半兽人镇
        else:
            print("当你沿着高隘口攀爬，希望避免被发现时，你听到了一些在阴影中爬行的声音....")
            input("按回车键继续。")
            print("")
            result = battle(player, constants.BattleEngineContext.STORY, self._wave.copy())
            if not result:
                return

            print("你打败了一些毫无戒心的半兽人！现在，你有机会尝试偷偷溜过去或直接攻入。")
            input("按回车键继续。")
            print("")

            # 征求用户选择
            print("一个选择是尝试冒着被围困的风险从咕噜的洞穴偷偷穿过去，另一个则是直接进入半兽人镇。")
            print("")
            choice = self._choice()

            # 运行与选择相关的脚本
            if choice == "cave":
                self._cave(player)
            else:
                self._frontalAssault(player)

    def _choice(self):
        """
        征求用户的选择。
        
        @return:     "cave" 或 "straight"
        """
        choice = None
        acceptable = ["cave", "straight"]
        while choice not in acceptable:
            choice = input("你打算怎么做？选择：偷偷溜过(cave)、直接进入(straight) ")
        print("")

        return choice

    def _cave(self, player):
        """
        咕噜洞穴的动作序列。
        
        @param player:  玩家对象
        """
        print("你试图潜入咕噜的洞穴。")
        input("按回车键继续。")
        print("")

        # 如果玩家冒险通过未被发现
        if random.random() < constants.GOBLIN_TOWN_EVASION_PROB:
            print("你安全地穿过了山脉！")
            input("按回车键继续。")
            print("")

        # 如果玩家被困在咕噜的洞穴中
        else:
            # 剧情
            print("半兽人王：“你这个笨蛋……你真的以为你能在我不知情的情况下闯过我的地盘吗？”")
            input("按回车键继续。")
            print("")

            # 遭到围困
            print("半兽人王：“现在我要吃你的肉……”")
            input("按回车键继续。")
            print("")
            result = battle(player, constants.BattleEngineContext.STORY, self._wave4.copy())
            if not result:
                return

            # 通关
            self._executed = True

        # 成功通过
        self._victorySequence(player)

    def _frontalAssault(self, player):
        """
        正面进攻。
        
        @param player:  玩家对象
        """
        # 剧情
        print("是时候杀死一些半兽人了! 前往半兽人镇!")
        input("按回车键继续。")
        print("")

        print("你看到了一些破败的小屋，都已无人居住。")
        input("按回车键继续。")
        print("")

        print("突然间，半兽人们从四面八方包围了你！")
        input("按回车键继续。")
        print("")

        # 正面突击第一波
        print("半兽人王：“谁给你的勇气直接冲进我的地盘？”")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave2.copy())
        if not result:
            return

        # 正面突击第二波
        print("半兽人王：“你这个愚蠢的傻瓜，现在你的死期到了！”")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave3.copy())
        if not result:
            return

        # 通关
        self._executed = True

        # 成功通过
        self._victorySequence(player)

    def _victorySequence(self, player):
        """
        成功通过半兽人镇。
        
        @param player:  玩家对象
        """
        location = player.getLocation()

        print("当你凝视着敌人的尸体时，你决定是时候带着你的战利品离开了。")
        input("按回车键继续。")
        print("")

        for item in self._loot:
            if not player.addToInventory(item):
                location.addItem(item)
        print("")

        self._createPort("south")
