#!/usr/bin/python
import constants

class Weapons(Item):
    """
    A class of weapons.
    """

    def __init__(self, damage):
        Item.__init__(self, name, description, weight)
        self._damage = damage

    def getType(self):
        """
        Returns the item's type.

        @return: Item's type.
        """
        return ItemType.WEAPON
