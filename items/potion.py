#!/usr/bin/python

from items.item import Item
from constants import ItemType


class Potion(Item):
    """
    Potion是Item的子类。
    
    药水是一种一次性使用的物品，用于治疗玩家。
    药水根据它们的healing参数的数值进行治疗。
    """

    def __init__(self, name, description, weight, cost, healing):
        """
        初始化药水对象。

        @param name:         药水名称
        @param description:  药水的描述
        @param weight:       药水的重量
        @param cost:         药水的价格
        @param healing:      药水的治疗量。使用时，玩家最多可以获得这个量的治疗
        """
        Item.__init__(self, name, description, weight, cost)

        self._healing = healing

    def getHealing(self):
        """
        返回药水的治疗量。

        @return: 药水的治疗量
        """
        return self._healing

    def getType(self):
        """
        返回物品的类型。

        @return: 物品的类型
        """
        return ItemType.POTION
