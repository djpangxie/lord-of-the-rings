#!/usr/bin/python

from items.item import Item

class ItemSet(object):
    """
    物品的集合。
    """
    def __init__(self, itemSet=None):
        """
        初始化一个 ItemSet 对象。

        @keyword itemSet:     (可选的)单个 Item 对象或 Item 对象列表
        """
        self._items = []
        self._weight = 0

        #收到的单件物品
        if isinstance(itemSet, Item):
            self.addItem(itemSet)
            
        #收到的一组物品
        elif isinstance(itemSet, list):
            self.addItems(itemSet)

    def addItem(self, item):
        """
        添加一个物品。

        @param item:    An item.
        """
        #检查前提条件
        if not isinstance(item, Item):
            errorMsg = "ItemSet.addItem() 传入的参数不是单件物品。"
            raise AssertionError(errorMsg)

        self._items.append(item)
        self._weight += item.getWeight()
        
    def addItems(self, items):
        """
        添加一组物品。
        
        @param items:    List of items.
        """
        #检查前提条件
        errorMsg = "ItemSet.addItems() 传入的参数不是一组物品。"
        if not isinstance(items, list):
            raise AssertionError(errorMsg)
            
        errorMsg = "ItemSet.addItems() 传入的一组物品中有的不是物品。"
        for item in items:
            if not isinstance(item, Item):
                raise AssertionError(errorMsg)
        
        #将列表中的项目添加到 ItemSet
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
        Gets an item with a given name.

        @param name:    Name of object.
        @return:        Item with given name.
                        Returns None if the item
                        cannot be found.
        """
        for item in self._items:
            if item.getName() == name:
                return item
                
        return None
    
    def removeItem(self, item):
        """
        Removes an item.

        @param item:    An item in this collection.
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
        Determines if item is contained in this collection.

        @param item:    An item.
        @return:        True if item is in this collection, False otherwise.
        """
        return (item in self._items)

    def containsItemWithName(self, itemName):
        """
        Determines if item is contained in this collection.
        
        @param itemName:     Items's name
        
        @return:             True if item with given name is present,
                             False otherwise
        """
        for item in self._items:
            if item._name == itemName:
                return True
                
        return False

    def count(self):
        """
        Returns the number of items.

        @return:    Number of items.
        """
        return len(self._items)

    def getWeight(self):
        """
        Determines total weight of items.

        @return:    Total weight of items.
        """
        return self._weight 
 
    def __iter__(self):
        """
        Provides an iterator for sets of items.
        """
        return iter(self._items)