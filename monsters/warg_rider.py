#!/usr/bin/python

import constants
from monsters.monster import Monster


class WargRider(Monster):
    """
    派生自Monster父类。

    在托尔金的宇宙中，座狼是野狼的一个品种，座狼骑手则是骑着座狼的奥克。
    """

    def __init__(self, stats):
        """
        初始化座狼骑手怪物。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.WargRider,
                         constants.MonsterDescriptions.WargRider, stats,
                         constants.MonsterAttackStrings.WargRider,
                         constants.MonsterDeathStrings.WargRider)
