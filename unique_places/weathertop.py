#!/usr/bin/python

from unique_place import UniquePlace
from monsters.nazgul import Nazgul
from battle_engine import battle
import constants
import random


class Weathertop(UniquePlace):
    """
    风云丘陵中的独特地点。在这里，玩家可以选择扎营。
    如果玩家决定扎营，他就有可能受到戒灵的攻击；如果这没有发生，玩家将被恢复到完全健康。
    """

    def __init__(self, name, description, greetings):
        """
        初始化风云顶。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)

        # 生成多只戒灵
        self._monsters = []
        numberNazgul = random.randrange(1, 8)
        for monster in range(numberNazgul):
            nazgul = Nazgul(constants.MONSTER_STATS[Nazgul])
            self._monsters.append(nazgul)

    def enter(self, player):
        """
        进入风云顶。

        @param player:  玩家对象
        """
        print(self._greetings)
        print("")

        print("尽管你实际对这个地方比较陌生，但你身处风云顶上时仍有一种强烈的似曾相识感。")
        input("按回车键继续。")

        # 征求用户输入
        choice = self._choice()

        # 运行用户相关序列
        if choice == "camp":
            self._camp(player)
        elif choice == "keep moving":
            print("你继续前行。")
            print("")

    def _choice(self):
        """
        征求用户选择
        """
        print("""
经过一天的旅行，你已经疲惫不堪。你想在风云顶扎营过夜吗？
\t“是的，我想扎营。”        - camp
\t“不，我将继续前行。”      - keep moving
""")
        choice = None
        acceptable = ["camp", "keep moving"]
        while choice not in acceptable:
            choice = input("你的选择是？ ")
        print("")

        return choice

    def _camp(self, player):
        """
        扎营动作序列。发生以下两种情况之一：
        -玩家被一群戒灵攻击。
        -玩家整晚安然无恙并得到完全康复。
        """
        # 遭遇戒灵
        if random.random() < constants.WEATHERTOP_BATTLE_PROB:
            print("当你准备好你的扎营用具时，你听到阴影中的一些沙沙声....")
            result = battle(player, constants.BattleEngineContext.STORY, self._monsters.copy())
            if not result:
                return

            print("唉，这下你不再敢再多休息了。")
            print("")

        # 安静的休息
        else:
            print("你在古老的废墟中安静地休息了一晚。")
            player.heal(player.getTotalMaxHp() - player.getHp())
            print("你醒来放松，准备出发！")
            print("")
