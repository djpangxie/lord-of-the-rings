#!/usr/bin/python

from items.item import Item
from constants import ItemType


class Charm(Item):
    """
    Charm是Item的子类。

    饰品可以修改任意数量的玩家属性。在《指环王》的所有饰品中，最突出的例子是魔戒，它可以改变多个玩家的状态。
    """

    def __init__(self, name, description, weight, cost, attack, defense, hp):
        """
        初始化饰品对象。

        @param name:         饰品名字
        @param description:  饰品的描述
        @param weight:       饰品的重量
        @param attack:       饰品的攻击加成
        @param defense:      饰品的防御加成
        @param hp:           饰品的生命值加成
        """
        Item.__init__(self, name, description, weight, cost)

        self._attack = attack
        self._defense = defense
        self._hp = hp

    def getAttack(self):
        """
        返回饰品的攻击加成。

        @return:    饰品的攻击加成
        """
        return self._attack

    def getDefense(self):
        """
        返回饰品的防御加成。

        @return:    防御加成
        """
        return self._defense

    def getHp(self):
        """
        返回饰品的生命值加成。

        @return:    饰品的生命值加成
        """
        return self._hp

    def getType(self):
        """
        返回物品的类型。

        @return:   物品的类型
        """
        return ItemType.CHARM
