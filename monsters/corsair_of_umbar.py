#!/usr/bin/python

import constants
from monsters.monster import Monster


class CorsairOfUmbar(Monster):
    """
    派生自Monster父类。

    在托尔金的宇宙中，昂巴海盗是在刚铎海岸附近劫掠的海盗。
    """

    def __init__(self, stats):
        """
        初始化昂巴海盗。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.CorsairOfUmbar,
                         constants.MonsterDescriptions.CorsairOfUmbar, stats,
                         constants.MonsterAttackStrings.CorsairOfUmbar,
                         constants.MonsterDeathStrings.CorsairOfUmbar)
