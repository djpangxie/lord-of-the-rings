#!/usr/bin/python

from .command import Command

class DropCommand(Command):
    """
    使玩家将物品从库存中放入当前地区。
    """
    def __init__(self, name, explanation, player):
        """
        初始化新的丢弃命令。

        @param name:         命令名称
        @param explanation:  命令的说明
        @param player:       玩家对象
        """
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Drops an item from inventory into space.
        """
        name = self._player.getName()
        inventory = self._player.getInventory()
        
        #Display inventory contents
        print("The following may be dropped by %s:" % name)
        for item in inventory:
            print("\t%s" % item.getName())
        print("")
        
        itemToRemove = input("Which item do you want to drop? \n")
        print("")
        
        #Create references
        equipped = self._player.getEquipped()
        item = inventory.getItemByName(itemToRemove)

        #Check if item is in inventory
        if not item:
            print("%s is not in your inventory!" % itemToRemove)
            return

        print("Dropping %s" % itemToRemove)
        print("Unequipping %s" % itemToRemove)
        
        inventory.removeItem(item)
        
        #If item is currently equipped
        if equipped.containsItem(item):
            equipped.removeItem(item)
        
        #Add item to space
        location = self._player.getLocation()
        location.addItem(item)