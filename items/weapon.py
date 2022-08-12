#!/usr/bin/python

from constants import ItemType
from items.item import Item


class Weapon(Item):
    """
    Weapon是Item的子类。
    
    武器作为游戏中的攻击型物品类别，定义了一个attack属性，它增加玩家攻击以构成玩家伤害。
    """

    def __init__(self, name, description, weight, cost, attack):
        """
        初始化武器对象。

        @param name:          武器名字
        @param description:   武器的描述
        @param weight:        武器的重量
        @param cost:          武器的价格
        @param attack:        武器的攻击力。装备武器时，玩家伤害会增加此数量
        """
        Item.__init__(self, name, description, weight, cost)

        self._attack = attack

    def getAttack(self):
        """
        返回武器的攻击力。

        @return:    武器的攻击力
        """
        return self._attack

    def getType(self):
        """
        返回物品的类型。

        @return: 物品的类型
        """
        return ItemType.WEAPON
