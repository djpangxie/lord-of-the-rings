#!/usr/bin/python

import constants
from monsters.monster import Monster


class Orc_II(Monster):
    """
    派生自Monster父类。
    
    在托尔金的宇宙中，奥克是索隆军队的主体力量。
    """

    def __init__(self, stats):
        """
        初始化奥克II怪物。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.Orc_II,
                         constants.MonsterDescriptions.Orc_II, stats,
                         constants.MonsterAttackStrings.Orc_II,
                         constants.MonsterDeathStrings.Orc_II)
