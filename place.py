#!/usr/bin/python

class Place(object):
    """
    城市和独特地点类的父类。
    """

    def __init__(self, name, description, greetings):
        """
        初始化地点对象。
        
        @param name:           地点名称
        @param description:    地点的描述
        @param greetings:      玩家进入该地点时得到的问候
        """
        self._name = name
        self._description = description
        self._greetings = greetings

    def getName(self):
        """
        返回地点名称。

        @return:    地点名称
        """
        return self._name

    def getDescription(self):
        """
        返回地点的描述。

        @return:    地点的描述
        """
        return self._description

    def getGreeting(self):
        """
        返回玩家进入该地点时得到的问候

        @return:    玩家进入该地点时得到的问候
        """
        return self._greetings

    def receiveSpaces(self, space, targetSpace):
        """
        创建该独特地点连接到的两个地区。

        @param space:         玩家的当前地区
        @param targetSpace:   通过该地点后将会去往的地区
        """
        self._space = space
        self._targetSpace = targetSpace

    def _createPort(self, direction):
        """
        在该地区和目标地区之间创建一个连接。在这个方法中，目标地区是指向的方向。
        在指环王中，这被用来解锁新的地区连接，作为通关剧情的奖励。
        
        @param direction:     "east"、"west"、"north"、"south"表示的目标地区的方向
        @param executed:      如果这个方法已经被执行过则为True，默认情况下为False
        """
        # 创建连接并打印附带的用户文本
        self._space.createExit(direction, self._targetSpace, outgoingOnly=False)
        print("%s 现在可以通往 %s" % (self._space.getName(), self._targetSpace.getName()))
        print("")

    def enter(self, player):
        """
        进入地点的方法，子类应该重写它。
        
        @param player:  玩家对象
        """
        print("这个enter方法应该被子类重写。")
