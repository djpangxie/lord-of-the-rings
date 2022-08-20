#!/usr/bin/python

from place import Place


class UniquePlace(Place):
    """
    派生自Place父类。
    
    地图上独一无二的地点。可能有任意数量的功能，包括战斗和故事互动。
    """

    def __init__(self, name, description, greetings):
        """
        初始化独特的地点对象
        
        @param name:            独特的地点名称
        @param description:     独特的地点的描述
        @param greetings:       玩家进入该独特的地点时得到的问候
        """
        Place.__init__(self, name, description, greetings)

    def enter(self, player):
        """
        当玩家进入该独特的地点时执行。

        @param player:  当前玩家
        """
        print(self._greetings)
