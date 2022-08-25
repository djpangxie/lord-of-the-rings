#!/usr/bin/python

from monsters.monster import Monster
import constants


class OrcArcher(Monster):
    """
    派生自Monster父类。
    
    在托尔金的宇宙中，奥克投矛手善于投掷长矛来远距离攻击。
    """

    def __init__(self, stats):
        """
        初始化奥克投矛手。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.OrcArcher,
                         constants.MonsterDescriptions.OrcArcher, stats,
                         constants.MonsterAttackStrings.OrcArcher,
                         constants.MonsterDeathStrings.OrcArcher)
