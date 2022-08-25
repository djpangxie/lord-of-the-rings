#!/usr/bin/python

from monsters.monster import Monster
import constants


class Sauroman(Monster):
    """
    派生自Monster父类。
    
    在托尔金的宇宙中，萨鲁曼是中土世界的巫师之首。
    """

    def __init__(self, stats):
        """
        初始化萨鲁曼怪物。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.Sauroman,
                         constants.MonsterDescriptions.Sauroman, stats,
                         constants.MonsterAttackStrings.Sauroman,
                         constants.MonsterDeathStrings.Sauroman)
