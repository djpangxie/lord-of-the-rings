#!/usr/bin/python

from monsters.monster import Monster
import constants


class MouthOfSauron(Monster):
    """
    派生自Monster父类。

    在托尔金的宇宙中，索隆之口是黑暗魔君索隆的首席特使。
    """

    def __init__(self, stats):
        """
        初始化索隆之口怪物。

        @param stats:     怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        """
        Monster.__init__(self, constants.MonsterNames.MouthOfSauron,
                         constants.MonsterDescriptions.MouthOfSauron, stats,
                         constants.MonsterAttackStrings.MouthOfSauron,
                         constants.MonsterDeathStrings.MouthOfSauron)
