#!/usr/bin/python

from unique_place import UniquePlace
from monsters.nazgul_ii import Nazgul_II
from monsters.orc import Orc
from monsters.orc_archer import OrcArcher
from monsters.troll import Troll
from monsters.black_numernorian import BlackNumernorian
from monsters.witch_king import WitchKing
from battle_engine import battle
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.item import Item
import constants

import random


class DolGuldur(UniquePlace):
    """
    多古尔都是黑森林南部的一个独特地点，其名称的意思是“妖术之山”。
    如果玩家访问多古尔都，他有机会与一些困难的怪物战斗并获得一些战利品。
    """

    def __init__(self, name, description, greetings):
        """
        初始化多古尔都。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)
        self._executed = False  # 通关记录

        self._wave = []
        self._wave2 = []
        self._wave3 = []

        # 创造第一波怪物
        for monster in range(11):
            monster = Orc(constants.MONSTER_STATS[Orc])
            self._wave.append(monster)
        for monster in range(10):
            monster = OrcArcher(constants.MONSTER_STATS[OrcArcher])
            self._wave.append(monster)
        for monster in range(7):
            monster = Troll(constants.MONSTER_STATS[Troll])
            self._wave.append(monster)

        # 创造第二波怪物
        numberNazgul = random.randrange(0, 8)
        for monster in range(numberNazgul):
            nazgul = Nazgul_II(constants.MONSTER_STATS[Nazgul_II])
            self._wave2.append(nazgul)
        if random.random() < constants.DOL_GULDUR_WITCH_KING_PROB:
            witchKing = WitchKing(constants.MONSTER_STATS[WitchKing])
            self._wave2.append(witchKing)
        for monster in range(8):
            monster = BlackNumernorian(constants.MONSTER_STATS[BlackNumernorian])
            self._wave2.append(monster)

        # 创造第三波怪物
        numberNazgul = random.randrange(0, 8)
        for monster in range(numberNazgul):
            nazgul = Nazgul_II(constants.MONSTER_STATS[Nazgul_II])
            self._wave3.append(nazgul)
        for monster in range(6):
            monster = BlackNumernorian(constants.MONSTER_STATS[BlackNumernorian])
            self._wave3.append(monster)

        # 生成战利品
        weapon = Weapon("诅咒之剑", "使你充满恐惧", 5, 18, 18)
        weapon2 = Weapon("诅咒之斧", "你光拿着就已经散失了获胜的信心", 5, 22, 16)
        armor = Armor("诅咒之盾", "其上已经千疮百孔", 5, 12, 1)
        potion = Potion("诅咒药剂", "一种不明物质", 2, 0, -10)
        item = Item("被诅咒的镜子", "只见奇怪的扭曲和阴影", 6, 18)
        item2 = Item("被诅咒的书籍", "魔典", 4, 72)
        self._loot = [weapon, weapon2, armor, potion, item, item2]

    def enter(self, player):
        """
        多古尔都的动作序列。
        
        @param player:   玩家对象
        """
        print(self._greetings)
        print("")

        # 已经通关了多古尔都
        if self._executed:
            print("你上次来时已经扫平了这里！")
            input("按回车键继续。")
            print("")
        # 尚未通关多古尔都
        else:
            # 征求用户选择
            choice = self._choice()

            # 执行用户选择的动作序列
            if choice == "frontal assault":
                self._frontalAssault(player)
            if choice == "escape":
                self._run(player)

    def _choice(self):
        """
        征求用户的选择。在这里，用户可以选择攻击或逃跑。
        """
        choice = None
        acceptable = ["frontal assault", "escape"]
        while choice not in acceptable:
            choice = input("你想要做什么？选择：正面进攻(frontal assault)、逃跑(escape) ")
        print("")

        return choice

    def _frontalAssault(self, player):
        """
        正面进攻选项的动作序列。
        
        @param player:   玩家对象
        """
        # 怪物战斗
        result = battle(player, constants.BattleEngineContext.STORY, self._wave.copy())
        if not result:
            return

        result = battle(player, constants.BattleEngineContext.STORY, self._wave2.copy())
        if not result:
            return

        # 通关
        self._executed = True

        # 胜利
        self._victorySequence(player)

    def _victorySequence(self, player):
        """
        夺取多古尔都的胜利序列。
        
        @param player:   玩家对象
        """
        location = player.getLocation()

        # 剧情
        print("虽然你已经扫平了多古尔都要塞，但深深的邪恶感仍然萦绕在这片土地上。")
        input("按回车键继续。")
        print("")

        # 获得战利品
        print("环顾四周，你发现了几样东西。")
        input("按回车键继续。")
        print("")
        for item in self._loot:
            if not player.addToInventory(item):
                location.addItem(item)
        print("")

        # 剧情
        print("你带着一种不祥的预感离开了这里。")
        print("")

    def _run(self, player):
        """
        逃跑选项的动作序列。
        
        @param player:   玩家对象
        """
        print("你发现自己被包围了。")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave3.copy())
        if not result:
            return

        print("你豁出性命的逃了出去！")
        print("")
