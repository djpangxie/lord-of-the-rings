#!/usr/bin/python

import constants
from monsters.monster import Monster


class BarrowWight(Monster):
    """
    派生自Monster父类。

    在托尔金的宇宙中，古冢尸妖是居住在古冢岗的恶灵。
    """

    def __init__(self, stats):
        """
        初始化古冢尸妖。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.BarrowWight,
                         constants.MonsterDescriptions.BarrowWight, stats,
                         constants.MonsterAttackStrings.BarrowWight,
                         constants.MonsterDeathStrings.BarrowWight)
