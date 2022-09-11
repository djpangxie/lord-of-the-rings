#!/usr/bin/python

import constants
from monsters.monster import Monster


class Nazgul(Monster):
    """
    派生自Monster父类。
    在托尔金的世界里，戒灵在整个系列中都纠缠着主角弗罗多。
    """

    def __init__(self, stats):
        """
        初始化戒灵怪物对象。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）。
        """
        Monster.__init__(self, constants.MonsterNames.Nazgul,
                         constants.MonsterDescriptions.Nazgul, stats,
                         constants.MonsterAttackStrings.Nazgul,
                         constants.MonsterDeathStrings.Nazgul)
