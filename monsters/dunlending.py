#!/usr/bin/python

import constants
from monsters.monster import Monster


class Dunlending(Monster):
    """
    派生自Monster父类。

    在托尔金的宇宙中，黑蛮地人是中土世界的原始人。
    """

    def __init__(self, stats):
        """
        初始化黑蛮地人。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.Dunlending,
                         constants.MonsterDescriptions.Dunlending, stats,
                         constants.MonsterAttackStrings.Dunlending,
                         constants.MonsterDeathStrings.Dunlending)
