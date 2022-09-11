#!/usr/bin/python

import constants
from monsters.monster import Monster


class Balrog(Monster):
    """
    派生自Monster父类。

    在托尔金的宇宙中，炎魔是中土世界最致命的生物之一。
    """

    def __init__(self, stats):
        """
        初始化炎魔怪物。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.Balrog,
                         constants.MonsterDescriptions.Balrog, stats,
                         constants.MonsterAttackStrings.Balrog,
                         constants.MonsterDeathStrings.Balrog)
