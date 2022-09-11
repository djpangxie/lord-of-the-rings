#!/usr/bin/python

import constants
from monsters.monster import Monster


class KingOfTheBarrows(Monster):
    """
    派生自Monster父类。
    在托尔金的宇宙中，尸妖王是掌管古冢岗的恶灵之王。
    """

    def __init__(self, stats):
        """
        初始化尸妖王。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.KingOfTheBarrows,
                         constants.MonsterDescriptions.KingOfTheBarrows, stats,
                         constants.MonsterAttackStrings.KingOfTheBarrows,
                         constants.MonsterDeathStrings.KingOfTheBarrows)
