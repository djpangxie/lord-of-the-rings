#!/usr/bin/python

from constants import ItemType
from items.item import Item


class Charm(Item):
    """
    Charm是Item的子类。

    饰品可以加减玩家属性值。在《指环王》的所有饰品中，最突出的例子是魔戒，它可以改变多个玩家的状态。
    """

    def __init__(self, name, description, weight, cost, attack, defense, hp):
        """
        初始化饰品对象。

        @param name:         饰品名字
        @param description:  饰品的描述
        @param weight:       饰品的重量
        @param cost:         饰品的价值
        @param attack:       饰品的攻击加值
        @param defense:      饰品的防御加值
        @param hp:           饰品的最大生命值加值
        """
        Item.__init__(self, name, description, weight, cost)

        self._attack = attack
        self._defense = defense
        self._hp = hp

    def getAttack(self):
        """
        返回饰品的攻击加值。

        @return:    饰品的攻击加值
        """
        return self._attack

    def getDefense(self):
        """
        返回饰品的防御加值。

        @return:    防御加值
        """
        return self._defense

    def getHp(self):
        """
        返回饰品的最大生命值加值。

        @return:    饰品的最大生命值加值
        """
        return self._hp

    def getType(self):
        """
        返回物品的类型。

        @return:   物品的类型
        """
        return ItemType.CHARM
