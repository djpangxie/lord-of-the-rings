#!/usr/bin/python

import constants
from monsters.monster import Monster


class SiegeWorks(Monster):
    """
    派生自Monster父类。
    
    索隆的攻城部队。
    """

    def __init__(self, stats):
        """
        初始化攻城部队。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.SiegeWorks,
                         constants.MonsterDescriptions.SiegeWorks, stats,
                         constants.MonsterAttackStrings.SiegeWorks,
                         constants.MonsterDeathStrings.SiegeWorks)
