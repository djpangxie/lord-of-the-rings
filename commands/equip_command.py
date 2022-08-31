#!/usr/bin/python

from .command import Command
from items.weapon import Weapon
from items.armor import Armor
from items.charm import Charm
from items.item_set import ItemSet


class EquipCommand(Command):
    """
    为玩家装备库存中的物品。
    """

    def __init__(self, name, explanation, player):
        """
        初始化装备命令。

        @param name:         命令名称
        @param explanation:  命令的说明
        @param player:       玩家对象
        """
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        为玩家装备库存中的物品。
        """
        # 创建变量
        inventory = self._player.getInventory()
        equipped = self._player.getEquipped()
        equippable = ItemSet()

        # 创建可装备物品清单
        for item in inventory:
            if (isinstance(item, Weapon) or isinstance(item, Armor) or isinstance(item, Charm)) and \
                    item not in equipped:
                equippable.addItem(item)

        # 如果没有可装备的物品
        if equippable.count() == 0:
            print("库存中没有可装备的物品。")
            return

        # 用户输入
        print("%s 可以装备：" % self._player.getName())
        for num, item in enumerate(equippable, 1):
            print("\t%d.%s" % (num, item.getName()))
        print("")

        while True:
            try:
                choice = input("输入装备的整数序号值：")
                choice = int(choice)
            except ValueError:
                choice = -1
            if 1 <= choice <= equippable.count():
                break
            else:
                print("装备序号输入有误！")

        # 装备上物品
        statement = self._player.equip(equippable.getItems()[choice - 1])
        print(statement)
