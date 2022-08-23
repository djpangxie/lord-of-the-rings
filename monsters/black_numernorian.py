#!/usr/bin/python

from monsters.monster import Monster
import constants


class BlackNumernorian(Monster):
    """
    派生自Monster父类。
    
    在托尔金的宇宙中，黑努曼诺尔人是强大的神秘主义者。
    """

    def __init__(self, stats):
        """
        初始化黑努曼诺尔人怪物。

        @param stats:     怪物基础数据的三元列表，包括生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.BlackNumernorian,
                         constants.MonsterDescriptions.BlackNumernorian, stats,
                         constants.MonsterAttackStrings.BlackNumernorian,
                         constants.MonsterDeathStrings.BlackNumernorian)
