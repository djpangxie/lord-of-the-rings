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


class BlackGate(UniquePlace):
    """
    魔栏农是死亡沼泽中的独特地点。
    
    魔栏农是进入魔多的最明确的途径。如果玩家访问黑门，他可以选择在黑门内战斗或逃跑。
    如果选择战斗，则必须与一波又一波的敌人战斗，以获得进入下一个地区的机会。
    如果选择逃跑，则仍然需要与少量的敌人战斗。
    """

    def __init__(self, name, description, greetings):
        """
        初始化独特地点对象。
        
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

        # 创建第一波怪物
        for monster in range(11):
            monster = Orc_II(constants.MONSTER_STATS[Orc_II])
            self._wave.append(monster)
        for monster in range(6):
            monster = OrcArcher_II(constants.MONSTER_STATS[OrcArcher_II])
            self._wave.append(monster)
        for monster in range(6):
            monster = Troll_II(constants.MONSTER_STATS[Troll_II])
            self._wave.append(monster)
        for monster in range(2):
            monster = BlackNumernorian_II(constants.MONSTER_STATS[BlackNumernorian_II])
            self._wave.append(monster)

        # 创建第二波怪物
        for monster in range(12):
            monster = Orc_II(constants.MONSTER_STATS[Orc_II])
            self._wave2.append(monster)
        for monster in range(6):
            monster = OrcArcher_II(constants.MONSTER_STATS[OrcArcher_II])
            self._wave2.append(monster)
        for monster in range(8):
            monster = Troll_II(constants.MONSTER_STATS[Troll_II])
            self._wave2.append(monster)
        for monster in range(4):
            monster = BlackNumernorian_II(constants.MONSTER_STATS[BlackNumernorian_II])
            self._wave2.append(monster)
        for monster in range(9):
            monster = Nazgul_III(constants.MONSTER_STATS[Nazgul_III])
            self._wave2.append(monster)

        # 创建第三波怪物
        for monster in range(6):
            monster = BlackNumernorian_II(constants.MONSTER_STATS[BlackNumernorian_II])
            self._wave3.append(monster)
        monster = MouthOfSauron(constants.MONSTER_STATS[MouthOfSauron])
        self._wave3.append(monster)

        # 创建第四波怪物
        for monster in range(8):
            monster = Orc_II(constants.MONSTER_STATS[Orc_II])
            self._wave4.append(monster)
        for monster in range(5):
            monster = OrcArcher_II(constants.MONSTER_STATS[OrcArcher_II])
            self._wave4.append(monster)
        for monster in range(3):
            monster = Troll_II(constants.MONSTER_STATS[Troll_II])
            self._wave4.append(monster)
        for monster in range(4):
            monster = BlackNumernorian_II(constants.MONSTER_STATS[BlackNumernorian_II])
            self._wave4.append(monster)

        # 创建战利品
        weapon = Weapon("奥克小刀", "老旧并成锯齿状", 4, 12, 8)
        armor = Armor("腐烂的靴子", "完全无用", 4, 0, 0)
        potion = Potion("奥克食物", "可能含有人肉", 2, 0, -15)
        potion2 = Potion("奥克饮料", "不知道里面含有些什么", 2, 0, -10)
        item = Item("奥克枕头", "就是一块石头", 3, 0)
        item2 = Item("奥克毛毯", "就是野兽的毛皮", 4, 2)
        self._loot = [weapon, armor, potion, potion2, item, item2]

    def enter(self, player):
        """
        黑门的动作序列。
        
        @param player:   玩家对象
        """
        # 剧情
        print(self._greetings)
        print("")

        # 已经攻下了魔栏农
        if self._executed:
            print("黑门现下由刚铎的英勇士兵们把守着。")
            input("按回车键继续。")
            print("")
        # 尚未攻下魔栏农
        else:
            print("“当你接近黑门时，几支奥克军队过来迎接你了！”")
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
        用户选择攻击或逃跑。
        """
        choice = None
        acceptable = ["frontal assault", "run"]
        while choice not in acceptable:
            choice = input("你想怎么做？选项：正面迎击(frontal assault)、逃跑(run) ")
        print("")

        return choice

    def _frontalAssault(self, player):
        """
        玩家正面迎击的动作序列。
        
        @param player:   玩家对象
        """
        # 第一波战斗
        print("索隆之口：“我真高兴你来了！”")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave.copy())
        if not result:
            return

        # 第二波战斗
        print("索隆之口：“嗯，你似乎不喜欢我们的牢房？”")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave2.copy())
        if not result:
            return

        # 第三波战斗
        print("索隆之口：“是时候去死了！”")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave3.copy())
        if not result:
            return

        # 调用胜利序列
        self._victorySequence(player)

    def _victorySequence(self, player):
        """
        玩家攻下了黑门的序列。
        
        @param player:   玩家对象
        """
        self._executed = True
        self._createPort("east")
        location = player.getLocation()

        print("你攻下了魔栏农，确保了进入魔多的西北路线畅通！")
        input("按回车键继续。")
        print("")

        print("在打扫战场时，你发现了许多物品。")
        input("按回车键继续。")
        print("")

        for item in self._loot:
            if not player.addToInventory(item):
                location.addItem(item)
        print("")

    def _run(self, player):
        """
        玩家尝试逃跑的动作序列。在这种情况下，一小部分敌人会追上玩家。
        
        @param player:   玩家对象
        """
        # 调用第四波敌军
        print("先锋部队追上了你。")
        input("按回车键继续。")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave4.copy())
        if not result:
            return

        # 剧情
        print("你躲过了其余的追兵！")
        input("按回车键继续。")
        print("")
