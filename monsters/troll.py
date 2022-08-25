#!/usr/bin/python

from monsters.monster import Monster
import constants


class Troll(Monster):
    """
    派生自Monster父类。

    在托尔金的宇宙中，食人妖都是力大无穷但智力低下的野兽。
    """

    def __init__(self, stats):
        """
        初始化食人妖怪物。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.Troll,
                         constants.MonsterDescriptions.Troll, stats,
                         constants.MonsterAttackStrings.Troll,
                         constants.MonsterDeathStrings.Troll)
