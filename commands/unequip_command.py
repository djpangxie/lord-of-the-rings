#!/usr/bin/python

from .command import Command

class UnequipCommand(Command):
    """
    卸下玩家当前装备的物品。
    """
    def __init__(self, name, explanation, player):
        """
        初始化卸下命令。

        @param name:         命令名称
        @param explanation:  命令的说明
        @param player:       玩家对象
        """
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Unequips player with item in inventory.
        """
        equipped = self._player.getEquipped()

        #If no items to unequip
        if equipped.count() == 0:
            print("No items to unequip.")
            return

        #User prompt
        print("%s may unequip:" % self._player.getName())
        for item in equipped:
            print("\t%s" % item.getName())
        print("")
        
        itemToUnequip = input("Which item do you want to unequip? \n")
        itemEquipment = equipped.getItemByName(itemToUnequip)
        
        #Check if item is currently equipped
        if not itemEquipment:
            print("")
            print("%s is not currently equipped!" % itemToUnequip)
            return

        #Unequips player with item
        statement = self._player.unequip(itemEquipment)
        print(statement)