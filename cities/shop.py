#!/usr/bin/python

from cities.building import Building
import factories.shop_factory
from items.item import Item
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.charm import Charm
from items.unique_items import theOneRing
from util.helpers import sortItems
import constants


class Shop(Building):
    """
    商店派生自建筑。
    商店是游戏中的市场。
    """

    def __init__(self, name, description, greetings, region, numItems, quality):
        """
        初始化商店

        @param name:        商店的名字
        @param description: 商店的描述
        @param greetings:   玩家进入商店时得到的问候
        @param region:      商店所处的地区
        @param numItems:    在商店里可以买到的物品数量
        @param quality:     可能在商店中买到的物品的品质。Ranges from 1-20.
        """
        Building.__init__(self, name, description, greetings)

        # 创建物品属性并生成物品对象
        self._region = region
        self._numItems = numItems
        self._quality = quality

        self._items = factories.shop_factory.getItems(region, numItems, quality)

        # 分类物品
        sortItems(self._items)

    def enter(self, player):
        """
        商店的行动序列。

        @param player:    玩家对象
        """
        print("")
        print("- - - %s - - -" % self._name)
        print("%s" % self._greetings)

        # 确定并执行玩家的选择
        choice = None
        while choice != "quit":
            print("""
你可以：
\t购买商品               -purchase
\t出售库存               -sell
\t退出                  -quit
""")
            choice = input("你想做什么？")
            print("")

            if choice == "purchase":
                self.buyItems(player)
            elif choice == "sell":
                self.sellItems(player)
            elif choice == "quit":
                self.leaveShop()
                break
            else:
                print("\"嗯？\"")

            print("")

    def buyItems(self, player):
        """
        从商店中购买物品。当商品被玩家买走后会从商店的商品列表中移除。

        @param player:     玩家对象
        """
        while True:
            # 如果商品已经售卖一空
            if self._items.count() == 0:
                print("商品已经售卖一空。")
                return

            # 列出商品
            print("可供购买的物品：")
            for num, item in enumerate(self._items, 1):
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

                # 打印商店中所有商品的信息
                print("\t%d.%s\t\t%s" % (num, itemName, itemDescription))

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

                print("重量：%-5s售价：%s\n" % (itemWeight, itemCost))

            print(
                "%s 目前拥有 %s%s 用来购买，取消购买请输入0" % (player.getName(), player.getMoney(), constants.CURRENCY))
            print("")

            # 用户输入
            while True:
                try:
                    choice = input("输入商品的整数序号值：")
                    choice = int(choice)
                except ValueError:
                    choice = -1
                if 1 <= choice <= self._items.count():
                    if player.getMoney() < self._items.getItems()[choice - 1].getCost():
                        print("你没有足够的金钱！")
                        continue
                    elif not player.addToInventory(self._items.getItems()[choice - 1]):
                        print("你不能背负该物品！")
                        continue
                    print("%s 购买了 %s" % (player.getName(), self._items.getItems()[choice - 1].getName()))
                    player.decreaseMoney(self._items.getItems()[choice - 1].getCost())
                    self._items.removeItem(self._items.getItems()[choice - 1])
                    break
                elif choice == 0:
                    return
                else:
                    print("商品序号输入有误！")

    def sellItems(self, player):
        """
        将玩家库存中的物品出售给商店。售出的物品都会添加到该商店的商品列表中。
        
        @param player:    玩家对象
        """
        inventory = player.getInventory()
        equipment = player.getEquipped()
        bonusDifficulty = player.getLocation().getBattleBonusDifficulty()

        while True:
            # 如果库存已经出售一空
            if inventory.count() == 0:
                print("库存已经出售一空。")
                return

            # 列出库存
            print("可以出售的物品：")
            for num, item in enumerate(inventory, 1):
                itemName = item.getName()
                itemDescription = item.getDescription()
                itemWeight = str(item.getWeight())
                itemCost = str(int(item.getCost() * constants.SELL_LOSS_PERCENTAGE * (1 - bonusDifficulty)))

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

                # 打印库存中所有物品的信息
                if item in equipment.getItems():
                    print("\t{:d}.*".format(num), end='')
                else:
                    print("\t{:d}.".format(num), end='')
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

                print("重量：%-5s收价：%s\n" % (itemWeight, itemCost))

            print(
                "%s 的当前负重为 %s/%s，取消出售请输入0" % (
                    player.getName(), inventory.getWeight(), player.getWeightLimit()))
            print("")

            # 用户输入
            while True:
                try:
                    choice = input("输入物品的整数序号值：")
                    choice = int(choice)
                except ValueError:
                    choice = -1
                if 1 <= choice <= inventory.count():
                    sellValue = int(inventory.getItems()[choice - 1].getCost() * constants.SELL_LOSS_PERCENTAGE * (
                            1 - bonusDifficulty))
                    print("%s 以 %s%s 售出了 %s" % (
                        player.getName(), sellValue, constants.CURRENCY, inventory.getItems()[choice - 1].getName()))
                    if inventory.getItems()[choice - 1] is theOneRing:
                        print("\n一些奇怪的人过来拿走了至尊戒。")
                    else:
                        self._items.addItem(inventory.getItems()[choice - 1])
                        sortItems(self._items)
                    player.increaseMoney(sellValue)
                    player.removeFromInventory(inventory.getItems()[choice - 1])
                    break
                elif choice == 0:
                    return
                else:
                    print("物品序号输入有误！")

    # 离开商店
    def leaveShop(self):
        print("你离开了%s。" % self._name)
