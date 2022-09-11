#!/usr/bin/python

import constants
from monsters.monster import Monster


class WitchKing(Monster):
    """
    派生自Monster父类。
    
    在托尔金的宇宙中，安格玛巫王是戒灵的领袖。
    """

    def __init__(self, stats):
        """
        初始化安格玛巫王怪物。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.WitchKing,
                         constants.MonsterDescriptions.WitchKing, stats,
                         constants.MonsterAttackStrings.WitchKing,
                         constants.MonsterDeathStrings.WitchKing)
