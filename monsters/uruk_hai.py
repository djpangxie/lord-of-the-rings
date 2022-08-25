#!/usr/bin/python

from monsters.monster import Monster
import constants


class UrukHai(Monster):
    """
    派生自Monster父类。
    
    在托尔金的宇宙中，乌鲁克族是人类和奥克的杂交品种。
    """

    def __init__(self, stats):
        """
        初始化乌鲁克族怪物。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.UrukHai,
                         constants.MonsterDescriptions.UrukHai, stats,
                         constants.MonsterAttackStrings.UrukHai,
                         constants.MonsterDeathStrings.UrukHai)
