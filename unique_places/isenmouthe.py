#!/usr/bin/python

from unique_place import UniquePlace
from monsters.nazgul_iii import Nazgul_III
from monsters.orc_ii import Orc_II
from monsters.orc_archer_ii import OrcArcher_II
from monsters.troll_ii import Troll_II
from monsters.black_numernorian_ii import BlackNumernorian_II
from monsters.mouth_of_sauron import MouthOfSauron
from battle_engine import battle
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.item import Item
import constants


class Isenmouthe(UniquePlace):
    """
    艾森毛兹是乌顿山谷中的独特地点
    在托尔金的宇宙中，它代表了缩小版的黑门。
    
    如果玩家进入艾森毛兹，他就有机会进入到戈埚洛斯平原（魔多的心脏）。
    """

    def __init__(self, name, description, greetings):
        """
        初始化艾森毛兹。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)
        self._executed = False  # 通关记录

        self._wave = []
        self._wave2 = []

        # 创建第一波怪物
        for monster in range(14):
            monster = Orc_II(constants.MONSTER_STATS[Orc_II])
            self._wave.append(monster)
        for monster in range(7):
            monster = OrcArcher_II(constants.MONSTER_STATS[OrcArcher_II])
            self._wave.append(monster)
        for monster in range(6):
            monster = Troll_II(constants.MONSTER_STATS[Troll_II])
            self._wave.append(monster)
        for monster in range(3):
            monster = BlackNumernorian_II(constants.MONSTER_STATS[BlackNumernorian_II])
            self._wave.append(monster)

        # 创建第二波怪物
        for monster in range(5):
            monster = Orc_II(constants.MONSTER_STATS[Orc_II])
            self._wave2.append(monster)
        for monster in range(4):
            monster = OrcArcher_II(constants.MONSTER_STATS[OrcArcher_II])
            self._wave2.append(monster)
        for monster in range(2):
            monster = Troll_II(constants.MONSTER_STATS[Troll_II])
            self._wave2.append(monster)
        for monster in range(5):
            monster = BlackNumernorian_II(constants.MONSTER_STATS[BlackNumernorian_II])
            self._wave2.append(monster)
        for monster in range(4):
            monster = Nazgul_III(constants.MONSTER_STATS[Nazgul_III])
            self._wave2.append(monster)
        monster = MouthOfSauron(constants.MONSTER_STATS[MouthOfSauron])
        self._wave2.append(monster)

        # 创建战利品
        weapon = Weapon("食人妖巨锤", "庞大而笨重", 18, 42, 20)
        armor = Armor("食人妖巨盾", "庞大而笨重", 14, 36, 2)
        potion = Potion("奥克吃食", "令人作呕", 2, 0, -15)
        potion2 = Potion("奥克饮品", "有潜在毒性", 2, 0, -20)
        item = Item("巨兽栅栏", "有潜在转卖价值", 5, 14)
        item2 = Item("螺钉和螺栓", "没啥用", 2, 4)
        self._loot = [weapon, armor, potion, potion2, item, item2]

    def enter(self, player):
        """
        艾森毛兹的动作序列。
        
        @param player:   玩家对象
        """
        print(self._greetings)
        print("")

        # 已经拿下了艾森毛兹
        if self._executed:
            print("艾森毛兹正由刚铎的突击队扫荡着。")
            input("按回车键继续。")
            print("")
        # 尚未拿下艾森毛兹
        else:
            print("当你靠近艾森毛兹时，看到有几支军队正在逼近。")
            input("按回车键继续。")
            print("")
            self._battle(player)

    def _battle(self, player):
        """
        艾森毛兹的战斗序列。
        
        @param player:   玩家对象
        """
        # 第一波战斗
        print("索隆之口：“你已经不再受欢迎了！”")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave.copy())
        if not result:
            return

        # 第二波战斗
        print("索隆之口：“是时候...去...死了！！！”")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave2.copy())
        if not result:
            return

        # 调用胜利序列
        self._victorySequence(player)

    def _victorySequence(self, player):
        """
        艾森毛兹的胜利序列。
        
        @param player:   玩家对象
        """
        self._executed = True
        location = player.getLocation()

        print("你确保了进入魔多的西北路线畅通！")
        input("按回车键继续。")
        print("")

        print("在打扫战场时，你发现了一些奇怪的物品。")
        input("按回车键继续。")
        print("")

        for item in self._loot:
            if not player.addToInventory(item):
                location.addItem(item)
        print("")

        print("欢迎去往魔多的心脏！")
        print("")

        self._createPort("south")
