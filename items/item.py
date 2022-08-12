#!/usr/bin/python

from constants import ItemType


class Item(object):
    """
    一个通用物品。可能由玩家持有，存在于房间等。
    物品有各种子类，例如武器和盔甲。
    """

    def __init__(self, name, description, weight, cost):
        """
        初始化一个物品对象

        @param name:          物品的名字
        @param description:   物品的描述
        @param weight:        物品的重量
        """
        if (not name) or (not description):
            raise AssertionError("物品必须有名称和描述。")
        if weight < 0:
            errorMsg = ("物品重量无效 (%s); 重量不能为负数。" % weight)
            raise AssertionError(errorMsg)
        if cost < 0:
            errorMsg = ("无效的物品费用 (%s); 费用不能是负数。" % cost)
            raise AssertionError(errorMsg)

        self._name = name
        self._description = description
        self._weight = weight
        self._cost = cost

    def getName(self):
        """
        获取物品的名称。

        @return: 物品的名称
        """
        return self._name

    def getDescription(self):
        """
        获取物品的描述。

        @return: 物品的描述
        """
        return self._description

    def getWeight(self):
        """
        获取物品的重量。

        @return: 物品的重量
        """
        return self._weight

    def getCost(self):
        """
        返回物品的价格。

        @return:    物品的价格
        """
        return self._cost

    def getType(self):
        """
        返回物品的类型。

        @attention: 这个方法必须被Item的所有子类重写(一个新的ItemType也必须在constants.py中定义)

        @return: 物品的类型
        """
        return ItemType.GENERIC
