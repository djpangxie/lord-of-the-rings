#!/usr/bin/python

import constants
from battle_engine import battle
from items.armor import Armor
from items.item import Item
from items.potion import Potion
from items.weapon import Weapon
from monsters.nazgul_iii import Nazgul_III
from monsters.orc_archer_ii import OrcArcher_II
from monsters.orc_ii import Orc_II
from monsters.troll_ii import Troll_II
from monsters.witch_king import WitchKing
from unique_place import UniquePlace


class MinasMorgul(UniquePlace):
    """
    米那斯魔古尔是埃斐尔度阿斯中的独特地点。
    在托尔金的宇宙中，这是一座被巫术俘虏的城市，也是戒灵的老巢。
    """

    def __init__(self, name, description, greetings):
        """
        初始化米那斯魔古尔。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)
        self._executed = False  # 通关记录

        self._wave = []
        self._wave2 = []
        self._wave3 = []

        # 创建第一波怪物
        for monster in range(13):
            monster = Orc_II(constants.MONSTER_STATS[Orc_II])
            self._wave.append(monster)
        for monster in range(8):
            monster = OrcArcher_II(constants.MONSTER_STATS[OrcArcher_II])
            self._wave.append(monster)
        for monster in range(7):
            monster = Troll_II(constants.MONSTER_STATS[Troll_II])
            self._wave.append(monster)

        # 创建第二波怪物
        for monster in range(8):
            monster = Nazgul_III(constants.MONSTER_STATS[Nazgul_III])
            self._wave2.append(monster)
        monster = WitchKing(constants.MONSTER_STATS[WitchKing])
        self._wave2.append(monster)

        # 创建第三波怪物
        for monster in range(7):
            monster = Orc_II(constants.MONSTER_STATS[Orc_II])
            self._wave3.append(monster)
        for monster in range(3):
            monster = OrcArcher_II(constants.MONSTER_STATS[OrcArcher_II])
            self._wave3.append(monster)
        for monster in range(4):
            monster = Nazgul_III(constants.MONSTER_STATS[Nazgul_III])
            self._wave3.append(monster)

        # 创建战利品
        description = "似乎有自己的想法"
        weapon = Weapon("魔古尔长刃", description, 6, 32, 18)
        description = "生锈了"
        weapon2 = Weapon("魔古尔短刃", description, 6, 18, 16)
        description = "完全没用"
        armor = Armor("腐烂的盾牌", description, 4, 6, 12)
        description = "对人类来说太小了"
        armor2 = Armor("旅行靴", description, 4, 4, 1)
        description = "含有奇怪的成分"
        potion = Potion("奥克红茶", description, 2, 0, -15)
        description = "恢复作用值得可疑"
        potion2 = Potion("奥克黑茶", description, 2, 0, -20)
        description = "有潜在转卖价值"
        item = Item("巨兽栅栏", description, 5, 42)
        self._loot = [weapon, weapon2, armor, armor2, potion, potion2, item]

    def enter(self, player):
        """
        米那斯魔古尔的动作序列。
        
        @param player:   玩家对象
        """
        print(self._greetings)
        print("")

        # 已经拿下了米那斯魔古尔
        if self._executed:
            print("米那斯魔古尔现下由刚铎的英勇士兵们驻守。")
            input("按回车键继续。")
            print("")
        # 尚未拿下米那斯魔古尔
        else:
            print("米那斯魔古尔的魔窟让人寒毛直竖。")
            input("按回车键继续。")
            print("")

            # 征求用户选择
            choice = self._choice()

            # 如果玩家选择正面攻击
            if choice == "frontal assault":
                self._frontalAssault(player)

            # 如果玩家选择逃跑
            if choice == "run":
                self._run(player)

    def _choice(self):
        """
        征求用户的选择。
        
        @return:      选项的字符串
        """
        choice = None
        acceptable = ["frontal assault", "run"]
        while choice not in acceptable:
            choice = input("你想做什么？选项：正面攻入(frontal assault)、逃跑(run) ")
        print("")

        return choice

    def _frontalAssault(self, player):
        """
        米那斯魔古尔的战斗序列。
        
        @param player:   玩家对象
        """
        # 第一波战斗
        print("安格玛巫王：“喝茶和吃小点心的时间到了。”")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave.copy())
        if not result:
            return

        print("安格玛巫王：“唔，你似乎不喜欢我的下午茶，真没礼貌....”")
        input("按回车键继续。")
        print("")

        # 第二波战斗
        print("安格玛巫王：“也许你会喜欢这个......”")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave2.copy())
        if not result:
            return

        # 调用胜利序列
        self._victorySequence(player)

    def _victorySequence(self, player):
        """
        米那斯魔古尔的胜利序列。
        
        @param player:   玩家对象
        """
        self._executed = True
        location = player.getLocation()

        print("你拿下了米那斯魔古尔，并确保了进入魔多的西部路线畅通！")
        input("按回车键继续。")
        print("")

        print("你迅速清扫了战场。")
        input("按回车键继续。")
        print("")

        for item in self._loot:
            if not player.addToInventory(item):
                location.addItem(item)
        print("")

        print("你迅速地继续前进，因为你知道索隆也在行动。")
        print("")

        self._createPort("east")

    def _run(self, player):
        """
        玩家选择逃跑时的动作序列。在这种情况下，玩家在离开时仍然会受到一小波敌人的攻击。
        
        @param player:   玩家对象
        """
        # 与敌人作战
        print("当你冲出该地区时，大量的敌人追上了你。")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave3.copy())
        if not result:
            return

        print("你勉强躲过了敌人的追杀。")
        print("")
