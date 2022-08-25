#!/usr/bin/python

from monsters.monster import Monster
import constants


class GreatGoblin(Monster):
    """
    派生自Monster父类。
    在托尔金的宇宙中，半兽人王是高隘口的半兽人首领。
    """

    def __init__(self, stats):
        """
        初始化一个半兽人王。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.GreatGoblin,
                         constants.MonsterDescriptions.GreatGoblin, stats,
                         constants.MonsterAttackStrings.GreatGoblin,
                         constants.MonsterDeathStrings.GreatGoblin)
