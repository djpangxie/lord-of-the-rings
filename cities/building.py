#!/usr/bin/python

class Building(object):
    """
    一个通用的建筑类，用于派生。建筑的子类包括旅店、商店和广场，这些子类有它们自己的一套方法。
    """

    def __init__(self, name, description, greetings):
        """
        初始化建筑对象。

        @param name:           建筑的名字
        @param description:    建筑的描述
        @param greetings:      玩家进入建筑时得到的问候
        """
        self._name = name
        self._description = description
        self._greetings = greetings

    def getName(self):
        """
        返回该建筑的名字

        @return:    建筑的名字的字符串
        """
        return self._name

    def getDescription(self):
        """
        返回该建筑的描述。

        @return:    建筑的描述的字符串
        """
        return self._description

    def greetings(self):
        """
        返回玩家进入建筑物时显示的字符串。

        @return:    玩家在进入建筑物时收到的问候的字符串
        """
        return self._greetings

    def enter(self, player):
        """
        默认的输入方法。默认情况下，不做任何事情。这个方法应该被子类所重写。

        @param player:   玩家对象
        """
        pass
