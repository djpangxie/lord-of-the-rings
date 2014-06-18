#!/usr/bin/python

from monsters.monster import Monster
import constants

class BlackNumernorian(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a BlackNumernorian monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.BlackNumernorian, constants.MonsterDescriptions.BlackNumernorian, stats, constants.MonsterAttackStrings.BlackNumernorian, constants.MonsterDeathStrings.BlackNumernorian) 