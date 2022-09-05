#!/usr/bin/python

from unique_place import UniquePlace
from monsters.nazgul_ii import Nazgul_II
from battle_engine import battle
from items.weapon import Weapon
from items.armor import Armor
from items.item import Item
import constants
import random


class Tharbad(UniquePlace):
    """
    沙巴德是米斯艾塞尔河中的独特地点。这是一座曾经有人居住的城市的遗迹。
    
    在这里，玩家可以选择探索废墟，探索废墟将使玩家能够冒着与戒灵遭遇的风险搜罗物品。
    """

    def __init__(self, name, description, greetings):
        """
        初始化沙巴德。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)

        # 生成玩家可以战斗的戒灵的列表
        self._monsters = []
        numberNazgul = random.randrange(1, 5)
        for monster in range(numberNazgul):
            nazgul = Nazgul_II(constants.MONSTER_STATS[Nazgul_II])
            self._monsters.append(nazgul)

        # 生成战利品
        description = "记载着古代的文字与符号"
        scroll = Item("古代卷轴", description, 1, 32)
        description = "看起来它随时都有可能断裂"
        weapon = Weapon("腐烂的法杖", description, 6, 3, 4)
        description = "也许被击打一两次就碎了"
        armor = Armor("腐烂的盾牌", description, 4, 2, 1)
        self._loot = [scroll, weapon, armor]

    def enter(self, player):
        """
        进入沙巴德。

        @param player:  玩家对象
        """
        # 剧情
        print(self._greetings)
        print("")

        print("你凝视着曾经的伟大城市沙巴德的古老遗迹，看到一些非常奇怪的景象。")
        input("按回车键继续。")
        print("")

        # 征求用户输入
        choice = None
        acceptable = ["explore", "leave"]
        while choice not in acceptable:
            choice = input("你想要做什么？选择：探索(explore)、离开(leave) ")
        print("")

        # 执行与用户相关的脚本
        if choice == "explore":
            self._explore(player)
        else:
            print("你告别了沙巴德的废墟，继续你的旅程。")
            print("")

    def _explore(self, player):
        """
        探索沙巴德的动作序列。

        @param player:   玩家对象
        """
        # 征求用户输入
        choice = None
        acceptable = ["ruined mill", "ancient bridge"]
        while choice not in acceptable:
            choice = input("你想去哪里探索？选项：毁坏的磨坊(ruined mill)、古老的桥梁(ancient bridge) ")
        print("")

        # 如果用户选择探索毁坏的磨坊
        if choice == "ruined mill":
            print("你发现很多腐烂的器具和农具的残骸。")
            input("按回车键继续。")
            print("")
            self._itemFind(player)
            if not self._chanceBattle(player):
                return
        # 如果用户选择探索古老的桥梁
        elif choice == "ancient bridge":
            print("你发现了在古代横跨南北的桥梁废墟。桥下是整个中土世界最伟大的堤道之一。")
            input("按回车键继续。")
            print("")
            self._itemFind(player)
            if not self._chanceBattle(player):
                return

        # 让玩家选择继续探索
        choice = None
        acceptable = ["yes", "no"]
        while choice not in acceptable:
            choice = input("你想继续探索吗？选项：是(yes)、否(no) ")
        print("")

        if choice == "yes":
            self._explore(player)
        else:
            print("你带着失落离开了沙巴德。")
            print("")

    def _chanceBattle(self, player):
        """
        决定是否要发生战斗。
        
        @param player:   玩家对象
        """
        if random.random() < constants.THARBAD_BATTLE_PROB:
            print("你听到阴影中的一些沙沙声......")
            input("按回车键继续。")
            print("")
            return battle(player, constants.BattleEngineContext.STORY, self._monsters.copy())
        else:
            return True

    def _itemFind(self, player):
        """
        判断玩家是否找到物品，然后给玩家该物品。
        
        @param player:   玩家对象
        """
        # 如果没有任何物品可供寻找
        if not self._loot:
            print("这里已经没什么有价值的东西了.....")
            print("")
            return

        # 确定玩家是否找到物品以及玩家收到的物品
        if random.random() < constants.THARBAD_ITEM_FIND_PROB:
            print("你找到了一些可能有价值的东西！")
            item = random.choice(self._loot)
            if player.addToInventory(item):
                self._loot.remove(item)
            print("")
