#!/usr/bin/python

from monsters.monster import Monster
import constants


class Orc(Monster):
    """
    派生自Monster父类。
    
    在托尔金的宇宙中，奥克是索隆军队的主体力量。
    """

    def __init__(self, stats):
        """
        初始化奥克怪物。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.Orc,
                         constants.MonsterDescriptions.Orc, stats,
                         constants.MonsterAttackStrings.Orc,
                         constants.MonsterDeathStrings.Orc)
