#!/usr/bin/python

import constants
from battle_engine import battle
from items.item import Item
from items.potion import Potion
from monsters.black_numernorian_ii import BlackNumernorian_II
from monsters.dragon_of_mordor import DragonOfMordor
from monsters.mouth_of_sauron import MouthOfSauron
from monsters.nazgul_iii import Nazgul_III
from monsters.orc_archer_ii import OrcArcher_II
from monsters.orc_ii import Orc_II
from monsters.troll_ii import Troll_II
from monsters.witch_king import WitchKing
from unique_place import UniquePlace


class BaradDur(UniquePlace):
    """
    巴拉督尔是戈埚洛斯平原中的独特地点。
    
    巴拉督尔是一个巨大的堡垒，玩家真的没有理由去参观。如果他去了，他就会遇到一波又一波的敌人。
    """

    def __init__(self, name, description, greetings):
        """
        初始化巴拉督尔。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)
        self._executed = False  # 通关记录

        self._wave = []
        self._wave2 = []
        self._wave3 = []
        self._wave4 = []
        self._wave5 = []

        # 创建第一波怪物
        for monster in range(12):
            monster = Orc_II(constants.MONSTER_STATS[Orc_II])
            self._wave.append(monster)
        for monster in range(7):
            monster = OrcArcher_II(constants.MONSTER_STATS[OrcArcher_II])
            self._wave.append(monster)
        for monster in range(5):
            monster = Troll_II(constants.MONSTER_STATS[Troll_II])
            self._wave.append(monster)
        for monster in range(3):
            monster = BlackNumernorian_II(constants.MONSTER_STATS[BlackNumernorian_II])
            self._wave.append(monster)

        # 创建第二波怪物
        for monster in range(15):
            monster = Orc_II(constants.MONSTER_STATS[Orc_II])
            self._wave2.append(monster)
        for monster in range(6):
            monster = OrcArcher_II(constants.MONSTER_STATS[OrcArcher_II])
            self._wave2.append(monster)
        for monster in range(10):
            monster = Troll_II(constants.MONSTER_STATS[Troll_II])
            self._wave2.append(monster)
        for monster in range(4):
            monster = BlackNumernorian_II(constants.MONSTER_STATS[BlackNumernorian_II])
            self._wave2.append(monster)

        # 创建第三波怪物
        for monster in range(5):
            monster = BlackNumernorian_II(constants.MONSTER_STATS[BlackNumernorian_II])
            self._wave3.append(monster)
        monster = MouthOfSauron(constants.MONSTER_STATS[MouthOfSauron])
        self._wave3.append(monster)

        # 创建第四波怪物
        for monster in range(8):
            monster = Nazgul_III(constants.MONSTER_STATS[Nazgul_III])
            self._wave4.append(monster)
        monster = WitchKing(constants.MONSTER_STATS[WitchKing])
        self._wave4.append(monster)

        # 创建第五波怪物
        for monster in range(14):
            monster = DragonOfMordor(constants.MONSTER_STATS[DragonOfMordor])
            self._wave5.append(monster)

        # 创建战利品
        potion = Potion("亢奋药剂", "具有超高的兴奋作用", 2, 112, 500)
        potion2 = Potion("超级药水", "超级奥克计划的产物", 2, 76, 350)
        potion3 = Potion("龙奶", "索隆平常喝的饮料", 2, 142, 1000)
        item = Item("大师球", "100%捕获任何宝可梦", 4, 272)
        item2 = Item("月之石", "进化普通的宝可梦", 6, 196)
        item3 = Item("金珠", "特别值钱", 12, 5000)
        self._loot = [potion, potion2, potion3, item, item2, item3]

    def enter(self, player):
        """
        巴拉督尔的动作序列。
        
        @param player:   玩家对象
        """
        # 已经清扫了巴拉督尔
        if self._executed:
            print("自你上次清扫过这里后，索隆似乎依旧蜷缩塔中。")
            input("按回车键继续。")
            print("")
        # 尚未清扫巴拉督尔
        else:
            print(self._greetings)
            print("")
            print("当你接近巴拉督尔时，成群的敌军如山呼海啸般向你压来！")
            input("按回车键继续。")
            print("")
            self._battle(player)

    def _battle(self, player):
        """
        巴拉督尔的战斗序列。玩家与五波敌人战斗。
        
        @param player:   玩家对象
        """
        print("奥克指挥官I：“这里没有你能通过的路！”")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave.copy())
        if not result:
            return

        print("奥克指挥官II：“%s，你不准再靠近了！”" % player.getName())
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave2.copy())
        if not result:
            return

        print("索隆之口：“你难道想成为邪黑塔的新主子？！”")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave3.copy())
        if not result:
            return

        print("九戒灵：“AAAAEEEEEEEEEEE!!!”")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave4.copy())
        if not result:
            return

        print("密密麻麻的魔多龙从四面八的上空朝你扑来！")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave5.copy())
        if not result:
            return

        # 调用胜利序列
        self._victorySequence(player)

    def _victorySequence(self, player):
        """
        巴拉督尔的胜利序列。玩家获得战利品。
        
        @param player:   玩家对象
        """
        self._executed = True
        location = player.getLocation()

        print("你来到了邪黑塔下，只见大门紧锁，毫无将要开启的迹象！")
        input("按回车键继续。")
        print("")

        print("黑暗魔君看来是选择了暂避锋芒，龟缩在塔楼之中....")
        input("按回车键继续。")
        print("")

        print("在清扫战场时，你发现了几个有趣的物品，但邪黑塔依然紧闭着。")
        input("按回车键继续。")
        print("")

        for item in self._loot:
            if not player.addToInventory(item):
                location.addItem(item)
        print("")
