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

    def _createPort(self, direction, executed=False):
        """
        Creates a port between the space and targetSpace. In this
        construction, targetSpace is to the direction of space.
        
        In LotR, this is used to unlock new space connections as a  
        reward for quest completion.
        
        @param direction:     The direction targetSpace is in with 
                              respect to space.
        @param executed:      If this method has been executed. False by 
                              default.
        """
        # If already executed, no need to create additional port
        self._executed = executed
        if self._executed:
            return

        # Create port and print accompanying user text
        self._space.createExit(direction, self._targetSpace,
                               outgoingOnly=False)
        string = "%s is now accessible to the %s" % (self._targetSpace.getName(),
                                                     direction)
        print(string.upper())
        print("")

        # Update self._executed
        self._executed = True

    def enter(self, player):
        """
        Parent enter method. Should be overridden by child classes.
        
        @param player:  The current player.
        """
        print("This enter method should be overridden by child class.")
