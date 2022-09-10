#!/usr/bin/python

from monsters.monster import Monster
import constants


class DragonOfMordor(Monster):
    """
    派生自Monster父类。
    
    在托尔金的宇宙中，龙是非常聪明的生物。
    """

    def __init__(self, stats):
        """
        初始化魔多龙怪物。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.DragonOfMordor,
                         constants.MonsterDescriptions.DragonOfMordor, stats,
                         constants.MonsterAttackStrings.DragonOfMordor,
                         constants.MonsterDeathStrings.DragonOfMordor)
