#!/usr/bin/python

import constants
from monsters.monster import Monster


class ArmoredMumakil(Monster):
    """
    派生自Monster父类。

    在托尔金的宇宙中，披甲毛象是为战争而训练的巨兽。
    """

    def __init__(self, stats):
        """
        初始化披甲毛象怪物。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.ArmoredMumakil,
                         constants.MonsterDescriptions.ArmoredMumakil, stats,
                         constants.MonsterAttackStrings.ArmoredMumakil,
                         constants.MonsterDeathStrings.ArmoredMumakil)
