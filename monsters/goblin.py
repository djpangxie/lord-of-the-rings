#!/usr/bin/python

import constants
from monsters.monster import Monster


class Goblin(Monster):
    """
    派生自Monster父类。
    在托尔金的宇宙中，半兽人是一种特殊的奥克。
    """

    def __init__(self, stats):
        """
        初始化一个半兽人怪物。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.Goblin,
                         constants.MonsterDescriptions.Goblin, stats,
                         constants.MonsterAttackStrings.Goblin,
                         constants.MonsterDeathStrings.Goblin)
