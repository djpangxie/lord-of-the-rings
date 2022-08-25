#!/usr/bin/python

from .command import Command
from items.weapon import Weapon
from items.armor import Armor
from items.charm import Charm

class CheckEquipmentCommand(Command):
    """
    显示玩家装备和详细的装备统计信息。
    """
    def __init__(self, name, explanation, player):
        """
        初始化新的检查装备命令。

        @param name:         命令名称
        @param explanation:  命令的说明
        @param player:       玩家对象
        """
        Command.__init__(self, name, explanation)
        
        self._player = player

    def execute(self):
        """
        Equips player with item in inventory.
        """
        playerName = self._player.getName()
        equipment = self._player.getEquipped()
        
        #Prints currently equipped items
        print("%s's currently equipped items:\n" % playerName)
        
        for item in equipment:
            itemName = item.getName()
            if isinstance(item, Weapon):
                attack = item.getAttack()
                print("\tWeapon: %s." % itemName)
                print("\t%s yields a %s attack bonus." % (itemName, attack))
            elif isinstance(item, Armor):
                defense = item.getDefense()
                print("\tArmor: %s." % itemName)
                print("\t%s yields a %s defense bonus." % (itemName, defense))
            elif isinstance(item, Charm):
                attack = item.getAttack()
                defense = item.getDefense()
                hp = item.getHp()
                print("\tCharm: %s:" % itemName)
                if item.getAttack():
                    print("\t%s yields a %s attack bonus." % (itemName, 
                    attack))
                if item.getDefense():
                    print("\t%s yields a %s defense bonus." % (itemName, 
                    defense))
                if item.getHp():
                    print("\t%s yields a %s HP bonus." % (itemName, hp))
            else:
                errorMsg = ("CheckEquipmentCommand command given invalid item" 
                " type.")
                raise AssertionError(errorMsg)
            print("")