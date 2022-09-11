#!/usr/bin/python

from items.item_set import ItemSet
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
        将物品从库存中放入地区。
        """
        name = self._player.getName()
        location = self._player.getLocation()
        equipped = self._player.getEquipped()
        inventory = self._player.getInventory()
        inventoryble = ItemSet()

        # 创建可丢弃物品清单
        for item in inventory:
            if not equipped.containsItem(item):
                inventoryble.addItem(item)

        # 如果没有可供丢弃的物品
        if inventoryble.count() == 0:
            print("库存中没有可丢弃的物品。")
            return

        # 用户输入
        print("%s 可以丢弃：" % name)
        for num, item in enumerate(inventoryble, 1):
            print("\t%d.%s" % (num, item.getName()))
        print("")

        while True:
            try:
                choice = input("输入物品的整数序号值：")
                choice = int(choice)
            except ValueError:
                choice = -1
            if 1 <= choice <= inventoryble.count():
                break
            else:
                print("物品序号输入有误！")

        # 丢弃物品
        location.addItem(inventoryble.getItems()[choice - 1])
        inventory.removeItem(inventoryble.getItems()[choice - 1])
