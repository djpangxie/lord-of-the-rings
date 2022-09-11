#!/usr/bin/python

import constants
from monsters.monster import Monster


class EliteUrukHai(Monster):
    """
    派生自Monster父类。
    
    这些是乌鲁克族精英战士。
    """

    def __init__(self, stats):
        """
        初始化乌鲁克族精英怪物。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.EliteUrukHai,
                         constants.MonsterDescriptions.EliteUrukHai, stats,
                         constants.MonsterAttackStrings.EliteUrukHai,
                         constants.MonsterDeathStrings.EliteUrukHai)
