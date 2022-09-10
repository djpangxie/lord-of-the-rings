#!/usr/bin/python

from unique_place import UniquePlace
from monsters.uruk_hai import UrukHai
from monsters.uruk_hai_archer import UrukHaiArcher
from monsters.elite_uruk_hai import EliteUrukHai
from monsters.sauroman import Sauroman
from battle_engine import battle
from items.item import Item
import constants
import random


class Isenguard(UniquePlace):
    """
    艾森加德是位于卡伦纳松的独特地点。它是萨鲁曼的要塞和基地。
    
    如果玩家访问艾森加德，他就有机会与一波又一波的敌人战斗，并获得一些战利品。
    """

    def __init__(self, name, description, greetings):
        """
        初始化艾森加德。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)
        self._executed = False  # 通关记录

        # 这里有三波怪物
        self._wave = []
        self._wave2 = []
        self._wave3 = []

        # 创建第一波怪物
        for monster in range(6):
            urukHai = UrukHai(constants.MONSTER_STATS[UrukHai])
            self._wave.append(urukHai)
        for monster in range(3):
            urukHaiArcher = UrukHaiArcher(constants.MONSTER_STATS[UrukHaiArcher])
            self._wave.append(urukHaiArcher)

        # 创建第二波怪物
        for monster in range(10):
            eliteUrukHai = EliteUrukHai(constants.MONSTER_STATS[EliteUrukHai])
            self._wave2.append(eliteUrukHai)
        for monster in range(4):
            urukHaiArcher = UrukHaiArcher(constants.MONSTER_STATS[UrukHaiArcher])
            self._wave2.append(urukHaiArcher)

        # 创建第三波怪物 - 乌鲁克族精英的基础数据翻倍了
        BONUS = 3
        increasedStats = []
        for stat in constants.MONSTER_STATS[EliteUrukHai]:
            increasedStats.append(stat * BONUS)
        for monster in range(2):
            eliteUrukHai = EliteUrukHai(increasedStats)
            self._wave3.append(eliteUrukHai)
        # 创建萨鲁曼
        sauroman = Sauroman(constants.MONSTER_STATS[Sauroman])
        self._wave3.append(sauroman)

        # 生成战利品
        description = "进入欧尔桑克石塔所需的两把巨大的黑色钥匙"
        self._keysOfOrthanc = Item("欧尔桑克的钥匙", description, 1, 104)
        self._palatir = Item("帕蓝提尔", "真知晶石", 6, 112)
        self._loot = [self._keysOfOrthanc, self._palatir]

    def enter(self, player):
        """
        进入艾森加德的动作序列。

        @param player:  玩家
        """
        print(self._greetings)
        print("")

        # 已经拿下了艾森加德
        if self._executed:
            print("你现在监管着艾森加德。")
            input("按回车键继续。")
            print("")
        # 尚未拿下艾森加德
        else:
            if not self._battle(player):
                return
            print("")

        # 玩家可以选择登上欧尔桑克石塔
        choice = self._summitPrompt()
        print("")

        # 执行用户相关脚本
        if choice == "yes":
            self._summitOrthanc(player)
        else:
            print("你继续你的旅程。")

    def _battle(self, player):
        """
        艾森加德的战斗序列。

        @param player:  玩家对象
        """
        # 第一波
        print("当你靠近艾森加德的环城时，立即受到一波乌鲁克族的欢迎......")
        input("按回车键继续。")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave.copy())
        if not result:
            return False
        print("")

        # 第二波
        print("当你凝视着被杀的敌人的尸体时，大巫师萨鲁曼出现了。")
        input("按回车键继续。")
        print("")

        print("萨鲁曼：“你不应该来，愚蠢的人。你难道傲慢到以为你能拿下欧尔桑克？”")
        input("按回车键继续。")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave2.copy())
        if not result:
            return False
        print("")

        # 第三波
        print("萨鲁曼：“你这个蠢货....”")
        input("按回车键继续。")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave3.copy())
        if not result:
            return False
        print("")

        # 胜利序列
        print("艾森加德今天有了新的监管者！")
        print("")

        self._executed = True
        self._createPort("south")
        location = player.getLocation()

        # 给玩家战利品
        if self._keysOfOrthanc in self._loot:
            print("你获得了欧尔桑克的钥匙！")
            print("")
            if player.addToInventory(self._keysOfOrthanc):
                self._loot.remove(self._keysOfOrthanc)
            else:
                location.addItem(self._keysOfOrthanc)

    def _summitPrompt(self):
        """
        征求用户的选择。玩家有机会登顶欧尔桑克石塔。

        @param player:  玩家对象
        """
        choice = None
        acceptable = ["yes", "no"]
        print("你想登上欧尔桑克石塔吗？")
        while choice not in acceptable:
            choice = input("选项：是(yes)、否(no) ")

        return choice

    def _summitOrthanc(self, player):
        """
        玩家登上欧尔桑克石塔的动作顺序。

        @param player:  玩家对象
        """
        # 登上欧尔桑克石塔
        print("你在欧尔桑克石塔中停留了片刻！")
        input("按回车键继续。")
        print("")

        # 玩家有机会找到欧尔桑克中最贵重的宝物
        if self._palatir in self._loot and random.random() < 0.3:
            print("你发现了欧尔桑克的晶石——帕蓝提尔")
            if player.addToInventory(self._palatir):
                self._loot.remove(self._palatir)
        print("")
