#!/usr/bin/python

from items.item_set import ItemSet
from items.potion import Potion
from .command import Command


class UsePotionCommand(Command):
    """
    使玩家在战斗之外使用药水。
    """

    def __init__(self, name, explanation, player):
        """
        初始化使用药水命令。

        @param name:         命令名称
        @param explanation:  命令的说明
        @param player:       玩家对象
        """
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        使用库存中的药水来治疗玩家。
        """
        # 检查库存中的药水
        inventory = self._player.getInventory()
        potions = ItemSet()

        for item in inventory:
            if isinstance(item, Potion):
                potions.addItem(item)
        if potions.count() == 0:
            print("%s 的库存中没有药水。" % self._player.getName())
            return

        # 用户提示
        print("%s 可以使用：" % self._player.getName())
        for num, potion in enumerate(potions, 1):
            print("\t%d.%-10s%10s点治疗量" % (num, potion.getName(), potion.getHealing()))
        print("")

        while True:
            try:
                choice = input("输入药水的整数序号值：")
                choice = int(choice)
            except ValueError:
                choice = -1
            if 1 <= choice <= potions.count():
                break
            else:
                print("药水序号输入有误！")

        # 治疗机制
        potionChoice = potions.getItems()[choice - 1]
        healing = potionChoice.getHealing()

        preHealedHealth = self._player.getHp()
        self._player.heal(healing)
        postHealedHealth = self._player.getHp()
        healed = postHealedHealth - preHealedHealth

        inventory.removeItem(potionChoice)

        print("%s 恢复了 %s 点生命值！ %s 的当前生命值为 %s " % (
            self._player.getName(), healed, self._player.getName(), self._player.getHp()))
