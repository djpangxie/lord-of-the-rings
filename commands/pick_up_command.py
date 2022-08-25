#!/usr/bin/python

from .command import Command

class PickUpCommand(Command):
    """
    使玩家从其当前地区中拾取物品。
    """
    def __init__(self, name, explanation, player):
        """
        初始化拾取命令。

        @param name:         命令名称
        @param explanation:  命令的说明
        @param player:       玩家对象
        """
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Picks up an item from a room and adds it to inventory.
        """
        name = self._player.getName()
        location = self._player.getLocation()
        locationItems = location.getItems()

        #User prompt
        print("The following may be picked up by %s:" % name)
        for item in locationItems:
            print("\t%s" % item.getName())
        print("")
        
        itemToAdd = input("Which item do you want to pick up? ")
        item = locationItems.getItemByName(itemToAdd)
        
        if not item:
            print("%s does not contain item." % location.getName())
            return

        #Successful execution
        if self._player.addToInventory(item):
            location.removeItem(item)