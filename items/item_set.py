#!/usr/bin/python

from items.item import Item


class ItemSet(object):
    """
    物品的集合。
    """

    def __init__(self, itemSet=None):
        """
        初始化一个 ItemSet 对象。

        @keyword itemSet:     (可选)单个Item对象或Item对象列表或ItemSet对象
        """
        self._items = []
        self._weight = 0

        # 收到的单件物品
        if isinstance(itemSet, Item):
            self.addItem(itemSet)
        # 收到的一组物品
        elif isinstance(itemSet, list):
            self.addItems(itemSet)
        elif isinstance(itemSet, ItemSet):
            self.addItems(itemSet.getItems())

    def addItem(self, item):
        """
        添加一个物品。

        @param item:    Item对象
        """
        # 检查前提条件
        if not isinstance(item, Item):
            errorMsg = "ItemSet.addItem() 传入的参数不是Item对象。"
            raise AssertionError(errorMsg)

        self._items.append(item)
        self._weight += item.getWeight()

    def addItems(self, items):
        """
        添加一组物品。
        
        @param items:    Item对象的列表
        """
        # 检查前提条件
        errorMsg = "ItemSet.addItems() 传入的参数不是列表。"
        if not isinstance(items, list):
            raise AssertionError(errorMsg)

        errorMsg = "ItemSet.addItems() 传入的列表中有的元素不是Item对象。"
        for item in items:
            if not isinstance(item, Item):
                raise AssertionError(errorMsg)

        # 将列表中的项目添加到 ItemSet
        for item in items:
            self.addItem(item)

    def getItems(self):
        """
        返回ItemSet中所包含的物品列表。

        @return:     ItemSet中所包含的物品列表
        """
        return self._items

    def getItemByName(self, name):
        """
        获取ItemSet中具有给定名称的Item对象。

        @param name:    对象名称
        @return:        具有给定名称的Item对象。如果找不到该物品，则返回None
        """
        for item in self._items:
            if item.getName() == name:
                return item

        return None

    def removeItem(self, item):
        """
        移除ItemSet中的某件物品。

        @param item:    此物品集中的某件物品
        """
        self._items.remove(item)
        self._weight -= int(item.getWeight())

    def clearItems(self):
        """
        清空ItemSet中所包含的物品列表。
        """
        self._items = []
        self._weight = 0

    def containsItem(self, item):
        """
        判断物品是否包含在此ItemSet集合中。

        @param item:    某物品
        @return:        如果物品在此集合中，则返回True，否则返回False
        """
        return (item in self._items)

    def containsItemWithName(self, itemName):
        """
        判断物品是否包含在此集合中。
        
        @param itemName:     物品名称
        
        @return:             如果ItemSet中存在具有给定名称的物品，则返回True，否则返回False
        """
        for item in self._items:
            if item._name == itemName:
                return True

        return False

    def count(self):
        """
        返回ItemSet中所有物品的总数。

        @return:    物品总数
        """
        return len(self._items)

    def getWeight(self):
        """
        返回ItemSet中所有物品的总重量。

        @return:    物品的总重量
        """
        return self._weight

    def __iter__(self):
        """
        返回ItemSet中所有物品的迭代器。
        """
        return iter(self._items)
