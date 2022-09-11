#!/usr/bin/python

import constants
from monsters.monster import Monster


class EasterlingWarrior(Monster):
    """
    派生自Monster父类。

    在托尔金的宇宙中，伊斯特林人是中洲以东地区的居民。
    """

    def __init__(self, stats):
        """
        初始化伊斯特林战士。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.EasterlingWarrior,
                         constants.MonsterDescriptions.EasterlingWarrior, stats,
                         constants.MonsterAttackStrings.EasterlingWarrior,
                         constants.MonsterDeathStrings.EasterlingWarrior)
