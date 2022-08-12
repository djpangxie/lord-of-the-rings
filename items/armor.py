#!/usr/bin/python

from items.item import Item
from constants import ItemType


class Armor(Item):
    """
    Armor是Item的子类。
    
    盔甲是游戏中的防御型物品类别，定义了一个defense属性，可以减少玩家受到的伤害。
    """

    def __init__(self, name, description, weight, cost, defense):
        """
        初始化盔甲对象。

        @param name:         盔甲名称
        @param description:  盔甲的描述
        @param weight:       盔甲的重量
        @param cost:         盔甲的价格
        @param defense:      盔甲的防御力
        """
        Item.__init__(self, name, description, weight, cost)

        self._defense = defense

    def getDefense(self):
        """
        返回盔甲的防御力。

        @return:    盔甲的防御力
        """
        return self._defense

    def getType(self):
        """
        返回物品的类型。

        @return:   物品的类型
        """
        return ItemType.ARMOR
