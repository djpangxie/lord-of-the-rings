#!/usr/bin/python

from items.item import Item
from items.item_set import ItemSet
from constants import Direction, RegionType
from items.unique_items import theOneRing

class Space(object):
    """
    地图上的给定地区。与其他地区相连，形成更大的地理区域。
    """
    def __init__(self, name, description, region, battleProbability = 0, battleBonusDifficulty = 0, items = None, city = None, uniquePlace = None):
        """
        初始化地区对象

        @param name:                   地区名称
        @param description:            地区的描述
        @param region                  地区类型的列举常量
        @param battleProbability:      在连续的游戏命令执行之间发生随机战斗的概率。在区间[0,1]之间
        @param battleBonusDifficulty:  该地区的难度加成，用于调整怪物属性与数量。在区间[-1,1]之间
                                       难度加成会使得该地区怪物的基础数据和基础生成量还有杀死其获得的经验、金钱按百分比加成。例如：
                                       难度加成为0.5的地区将产生150%基础生成量的具有150%基础属性的怪物，它被杀死后获得150%经验、金钱
        @keyword items:                (可选)地区中的物品。可以是单个Item对象或Item对象列表或ItemSet对象
        @keyword city:                 (可选)地区中的城市。可以是单个对象或包含多个对象的列表
        @keyword uniquePlace:          (可选)地区中的独特地点。可以是单个对象或包含多个对象的列表
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
        #至尊戒的特别提醒
        if item == theOneRing and self._name != "欧洛都因":
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
        返回地区中的城市。

        @return:    城市对象或包含多个城市对象的列表
        """
        return self._city

    def getUniquePlace(self):
        """
        返回地区中的独特地点。

        @return:    独特地点对象或包含多个独特地点对象的列表
        """
        return self._uniquePlace

    def getBattleProbability(self):
        """
        返回在该地区旅行时发生随机战斗的概率。

        @return:    随机战斗发生的概率
        """
        return self._battleProbability

    def getBattleBonusDifficulty(self):
        """
        返回该地区的难度加成。

        @return:    地区的难度加成
        """
        return self._battleBonusDifficulty

    def createExit(self, direction, space, outgoingOnly = False):
        """
        创建通往另一个地区的出口。一个地区的每个方向都可以通向一个或多个地区。
        默认情况下，该方法会在该出口连接的地区中同时创建适当的出口回到该地区。(然而，可以使用outgoingOnly参数来抑制这种情况)

        @param direction:       出口方向
        @param space:           连接的地区
        @keyword outgoingOnly:  默认情况下，该方法会在该出口连接的地区中同时创建适当的出口回到该地区
                                将outgoingOnly参数设置为True可以抑制这种情况
        """
        #确保指定的方向有效
        if not self._isExit(direction):
            errorMsg = "方向无效：%s" % direction
            raise AssertionError(errorMsg)
        
        #设置出口连接的地区
        if self._exits[direction]:
            currentSpace = self._exits[direction]
            #如果该方向已存在多个地区
            if isinstance(currentSpace, list):
                currentSpace.append(space)
            #如果该方向只存在一个地区
            else:
                self._exits[direction] = [currentSpace, space]
        #如果还没有连接到任何地区
        else:
            self._exits[direction] = space

        #创建从其它地区到该地区的出口
        if not outgoingOnly:
            oppositeDirection = self._oppositeDirection(direction)
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
        返回对相邻地区对象的引用。如果在给定方向的出口上不存在地区，则返回None。

        @param direction:   相邻地区的方向。必须是constants.Direction中定义的方向之一
        
        @return:            给定方向的地区对象（如果给定方向没有地区则为None）
        """
        return self._exits[direction]

    def getExits(self):
        """
        返回该地区所有方向连接的字典。

        @return:            方向连接的字典
        """
        return self._exits

    def _isExit(self, exit):
        """
        确保出口字符串代表一个有效的出口。

        @param direction:   出口名称

        @return:            如果有效则返回True，否则返回False
        """
        availableExits = list(self._exits.keys())
        if exit not in availableExits:
            return False
            
        return True

    def _oppositeDirection(self, direction):
        """
        返回相反的方向。(例如：北与南相反)

        @param direction:   一个方向
        
        @return:            相反的方向
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
            raise AssertionError("该方向无效：%s" % direction)