#!/usr/bin/python

import constants
from monsters.monster import Monster


class Nazgul_III(Monster):
    """
    派生自Monster父类。

    在托尔金的宇宙中，戒灵在整个魔戒大战系列中都纠缠着主要人物弗罗多。
    戒灵III是在游戏后期出现的最强的戒灵。
    """

    def __init__(self, stats):
        """
        初始化戒灵III怪物。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.Nazgul_III,
                         constants.MonsterDescriptions.Nazgul_III, stats,
                         constants.MonsterAttackStrings.Nazgul_III,
                         constants.MonsterDeathStrings.Nazgul_III)
