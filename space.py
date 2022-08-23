#!/usr/bin/python

from items.item import Item
from items.item_set import ItemSet
from constants import Direction, RegionType
from items.unique_items import theOneRing

class Space(object):
    """
    地图上的给定位置。与其他空间相连，形成更大的地理区域。
    """
    def __init__(self, name, description, region, battleProbability = 0, battleBonusDifficulty = 0, items = None, city = None, uniquePlace = None):
        """
        初始化地区对象

        @param name:                   地区名称
        @param description:            地区的描述
        @param region                  地区类型的列举常量
        @param battleProbability:      在连续的游戏命令执行之间发生随机战斗的概率。在区间[0,1]之间
        @param battleBonusDifficulty:  该地区的奖励难度，用于调整战斗与奖励的加成。在区间[0,1]之间
                                       此统计数据会导致任何给定区域的默认怪物统计数据和数量的百分比增加
                                       例如：如果奖励难度设置为0.5，该地区将产生50%更多具有150%基础属性的怪物
        @keyword items:                (可选)在地区中能找到的物品。可以是单个Item对象或Item对象列表或ItemSet对象
        @keyword city:                 (可选)地区中的城市。可以是单个对象或包含多个对象的列表
        @keyword uniquePlace:          (可选)地区中独特地点。可以是单个对象或包含多个对象的列表
        """
        self._exits = {Direction.NORTH : None,
                       Direction.SOUTH : None,
                       Direction.EAST : None,
                       Direction.WEST : None}

        self._name = name
        self._description = description
        self._region = region
        self._battleProbability = battleProbability
        self._battleBonusDifficulty = battleBonusDifficulty
        self._items = ItemSet(items)
        self._city = city
        self._uniquePlace = uniquePlace

    def getName(self):
        """
        返回地区名称。

        @return:    地区名称
        """
        return self._name

    def getDescription(self):
        """
        返回地区的描述。

        @return:    地区的描述
        """
        return self._description
        
    def getRegion(self):
        """
        返回地区类型的列举常量。
        
        @return:    地区类型的列举常量
        """
        return self._region
        
    def getItems(self):
        """
        返回在地区中能找到的物品。

        @return:    在地区中能找到的物品的ItemSet对象
        """
        return self._items
        
    def addItem(self, item):
        """
        添加一件或多件物品到该地区中。

        @param item:    要添加的一件或多件物品
        """
        #至尊魔戒的特别提醒
        if item == theOneRing and self._name != "Orodruin":
            print("\n你看到一些奇怪的人走过。")
            return

        if isinstance(item, Item):
            self._items.addItem(item)
        elif isinstance(item, list):
            self._items.addItems(item)
        elif isinstance(item, ItemSet):
            self._items.addItems(item.getItems())
        else:
            errorMsg = "space.AddItem() 传入了无效的物品类型。"
            raise AssertionError(errorMsg)

    def removeItem(self, item):
        """
        从该地区中删除一个物品。

        @param item:    要删除的物品
        """
        self._items.removeItem(item)

    def containsItem(self, item):
        """
        判断地区中是否包含物品。

        @param item:    要搜索的Item对象

        @return:    如果Item对象包含在该地区中，则返回True，否则返回False
        """
        return self._items.containsItem(item)

    def containsItemString(self, string):
        """
        Determines if space contains an item.

        @param string:   The name-string of 
                         the target item.

        @return:    True if item is contained 
                    in space, False otherwise.
        """ 
        return        self._items.containsItemWithName(string)
    
    def getCity(self):
        """
        Returns city object/objects.

        @return:    Reference to cit(ies).
                    May refer to a single city or list of cities.
        """
        return self._city

    def getUniquePlace(self):
        """
        Returns uniquePlace object(s).

        @return:    Reference to unique place(s).
                    May be reference to a single unique
                    place or a list of unique places.
        """
        return self._uniquePlace

    def getBattleProbability(self):
        """
        Returns probability of a random battle.

        @return:    The probability that a random
                    battle occurs.
        """
        return self._battleProbability

    def getBattleBonusDifficulty(self):
        """
        Returns bonus difficulty attribute of space.

        @return:    The difficulty parameter of space.
        """
        return self._battleBonusDifficulty

    def createExit(self, direction, space, outgoingOnly = False):
        """
        Create an exit to another space. By default, the method creates the 
        appropriate exit in the second space. (This can be suppressed, however, 
        using I{outgoingOnly}).
        
        Spaces can have multiple spaces per direction.

        @param direction:       Direction of exit.
        @param space:           Adjacent space.
        @keyword outgoingOnly:  By default, this method creates the appropriate
                                exit in the second space. Set I{outgoingOnly}
                                to False to suppress this behaviour.
        """
        #Make sure a valid direction has been specified
        if not self._isExit(direction):
            errorMsg = "Direction not valid: %s" % direction
            raise AssertionError(errorMsg)
        
        #Set exit to other space - if a space already exists
        if self._exits[direction]:
            currentSpace = self._exits[direction]
            #If multiple spaces already exist in that direction
            if isinstance(self._exits[direction], list):
                currentSpace.append(space)
            #If a single space exists in that direction
            else:
                self._exits[direction] = [currentSpace, space]
        #If no space already exists
        else:
            self._exits[direction] = space

        #Create exit from other space to this space
        if not outgoingOnly:
            oppositeDirection = self._oppositeDirection(direction)
            #outgoingOnly = True as to not create an infinite loop
            space.createExit(oppositeDirection, self, outgoingOnly = True)

    def clearExit(self, direction, outgoingOnly, space = None):
        """
        Removes an exit to another space. By default, the method removes the 
        appropriate exit from the second space. (This can be suppressed, 
        however, using I{outgoingOnly}).

        @param direction:       Direction of exit.
        @keyword outgoingOnly:  By default, this method removes the appropriate
                                exit from the second space. Set I{outgoingOnly}
                                to False to suppress this behavior.
        """
        #Make sure a valid direction has been specified
        if not self._isExit(direction):
            errorMsg = "Direction not valid: %s" % direction
            raise AssertionError(errorMsg)

        #If exit has not been set, there is nothing to do
        if self._exits[direction] == None:
            return
    
        #Create a temporary copy of adjacent space
        adjSpace = self._exits[direction]
        
        if isinstance(self._exits[direction], list):
            self._exits[direction].remove(space)
        else:
            self._exits[direction] = None
            
        if not outgoingOnly:
            oppositeDirection = self._oppositeDirection(direction)
            adjSpace.clearExit(oppositeDirection, True, space = self)

    def getExit(self, direction):
        """
        Returns a reference to an adjacent space.
        Returns None if no space exists in given direction.

        @param direction:   Direction of adjacent space.
                            Must be one of the directions defined in
                            constants.Direction.
        
        @return:            Reference to space in given direction.
                            (Returns None if no exit is defined
                            for given direction).
        """
        space = self._exits[direction]
        return space

    def getExits(self):
        """
        Returns dictionary of direction-space pairs.

        @return:            Dictionary of direction-space pairs.
        """
        return self._exits

    def _isExit(self, exit):
        """
        Makes sure that a string represents a valid exit.

        @param direction:   Name of exit.

        @return:            True if valid exit, False otherwise.
        """
        availableExits = list(self._exits.keys())
        if exit not in availableExits:
            return False
            
        return True

    def _oppositeDirection(self, direction):
        """
        Returns the opposite direction. (e.g. North is opposite of South)

        @param direction:   A direction (from constants.Direction)
        
        @return:            Opposite direction (from constants.Direction)
        """
        if direction == Direction.NORTH:
            return Direction.SOUTH
        elif direction == Direction.SOUTH:
            return Direction.NORTH
        elif direction == Direction.EAST:
            return Direction.WEST
        elif direction == Direction.WEST:
            return Direction.EAST
        else:
            raise AssertionError("Not a valid direction: %s" % direction)