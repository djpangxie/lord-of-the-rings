#!/usr/bin/python

from items.armor import Armor
from items.charm import Charm
from items.item import Item
from items.potion import Potion
from items.weapon import Weapon
from .command import Command


class CheckInventoryCommand(Command):
    """
    显示玩家库存和详细物品统计信息。
    """

    def __init__(self, name, explanation, player):
        """
        初始化新的检查库存命令。

        @param name:         命令名称
        @param explanation:  命令的说明
        @param player:       玩家对象
        """
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        显示角色库存。
        """
        # 获取玩家基本信息
        playerName = self._player.getName()
        inventory = self._player.getInventory()
        inventoryList = inventory.getItems()
        equipment = self._player.getEquipped()
        equipmentList = equipment.getItems()

        # 循环浏览玩家的库存，获取物品统计信息
        print("%s的库存：\n" % playerName)
        for item in inventoryList:
            itemName = item.getName()
            itemDescription = item.getDescription()
            itemWeight = str(item.getWeight())
            itemCost = str(item.getCost())

            if isinstance(item, Armor):
                itemDefense = str(item.getDefense())
            elif isinstance(item, Weapon):
                itemAttack = str(item.getAttack())
            elif isinstance(item, Potion):
                itemHeal = str(item.getHealing())
            elif isinstance(item, Charm):
                itemDefense = str(item.getDefense())
                itemAttack = str(item.getAttack())
                itemHp = str(item.getHp())
            elif isinstance(item, Item):
                pass
            else:
                errorMsg = "某件物品的类型有误！"
                raise AssertionError(errorMsg)

            # 打印库存中给定物品的信息
            if item in equipmentList:
                print("\t*", end='')
            else:
                print("\t", end='')
            print("%s\t\t%s" % (itemName, itemDescription))

            if isinstance(item, Weapon):
                print("\t攻击力：%-5s" % itemAttack, end='')
            elif isinstance(item, Armor):
                print("\t防御力：%-5s" % itemDefense, end='')
            elif isinstance(item, Potion):
                print("\t治疗量：%-5s" % itemHeal, end='')
            elif isinstance(item, Charm):
                print("\t攻击加值：%-5s防御加值：%-5sHP加值：%-5s" % (itemAttack, itemDefense, itemHp), end='')
            elif isinstance(item, Item):
                print("\t", end='')
            else:
                errorMsg = "某件物品的类型有误！"
                raise AssertionError(errorMsg)

            print("重量：%-5s价格：%s\n" % (itemWeight, itemCost))

        print("当前库存总重量：%s" % inventory.getWeight())
