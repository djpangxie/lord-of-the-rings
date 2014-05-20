#!/usr/bin/python

from monsters.monster import Monster

class Nazgul(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a Nazgul monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        self._name = "Nazgul"
        self._description = "\"AAAAEEEEEEEEEEE!!!\""
        self._hp = stats[0]
        self._attack = stats[1]
        self._experience = stats[2]
        self._attackString = "cleaved at you"
        self._deathString = "\"AAAAEEEEEEEEEEE!!!\""