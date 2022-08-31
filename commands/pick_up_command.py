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
        从地区中拾取物品并将其添加到库存中。
        """
        name = self._player.getName()
        location = self._player.getLocation()
        locationItems = location.getItems()

        # 如果没有可供拾取的物品
        if locationItems.count() == 0:
            print("地区中没有可拾取的物品。")
            return

        # 用户输入
        print("%s 可以拾取：" % name)
        for num, item in enumerate(locationItems, 1):
            print("\t%d.%s" % (num, item.getName()))
        print("")

        while True:
            try:
                choice = input("输入物品的整数序号值：")
                choice = int(choice)
            except ValueError:
                choice = -1
            if 1 <= choice <= locationItems.count():
                break
            else:
                print("物品序号输入有误！")

        # 拾取物品
        if self._player.addToInventory(locationItems.getItems()[choice - 1]):
            location.removeItem(locationItems.getItems()[choice - 1])
