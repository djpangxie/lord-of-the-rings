#!/usr/bin/python

from .command import Command
from space import Space
from cities.city import City
from unique_place import UniquePlace
import constants


class MapCommand(Command):
    """
    地图命令。
    """

    def __init__(self, name, explanation, player):
        """
        初始化地图命令。

        @param name:            命令名称
        @param explanation:     命令的说明
        @param player:          玩家对象
        """
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        显示连接到玩家当前地区的每个地区及其中的地点。
        """
        # 为地图位置生成变量
        location = self._player.getLocation()
        exits = location.getExits()

        print("由 %s 可以去往：" % location.getName())

        # 按北、南、东、西的顺序列出每个地区的详细信息
        if exits[constants.Direction.NORTH]:
            space = exits[constants.Direction.NORTH]
            # 对于单个地区
            if not isinstance(space, list):
                self._printInformation(space, constants.Direction.NORTH)
            # 对于多个地区
            else:
                for individualSpace in space:
                    self._printInformation(individualSpace, constants.Direction.NORTH)

        if exits[constants.Direction.SOUTH]:
            space = exits[constants.Direction.SOUTH]
            # 对于单个地区
            if not isinstance(space, list):
                self._printInformation(space, constants.Direction.SOUTH)
            # 对于多个地区
            else:
                for individualSpace in space:
                    self._printInformation(individualSpace, constants.Direction.SOUTH)

        if exits[constants.Direction.EAST]:
            space = exits[constants.Direction.EAST]
            # 对于单个地区
            if not isinstance(space, list):
                self._printInformation(space, constants.Direction.EAST)
            # 对于多个地区
            else:
                for individualSpace in space:
                    self._printInformation(individualSpace, constants.Direction.EAST)

        if exits[constants.Direction.WEST]:
            space = exits[constants.Direction.WEST]
            # 对于单个地区
            if not isinstance(space, list):
                self._printInformation(space, constants.Direction.WEST)
            # 对于多个地区
            else:
                for individualSpace in space:
                    self._printInformation(individualSpace, constants.Direction.WEST)

    def _printInformation(self, space, direction):
        """
        打印地区的名称，并列出它可能拥有的任何城市和独特地点。
        
        @param space:               地区对象
        @param direction:           地区相对于玩家当前位置的方向
        """
        # 指出地区
        spaceName = space.getName()
        print("\t%-10s地区：%s" % (direction, spaceName), end='')

        # 如果地区中存在城市
        cities = space.getCity()
        if cities:
            if isinstance(cities, City):
                cityName = cities.getName()
                print("\t\t城市：%s" % cityName, end='')
            elif isinstance(cities, list):
                for city in cities:
                    cityName = city.getName()
                    print("\t\t城市：%s" % cityName, end='')

        # 如果地区中存在独特地点
        if space.getUniquePlace():
            uniquePlaces = space.getUniquePlace()
            if isinstance(uniquePlaces, UniquePlace):
                uniquePlaceName = uniquePlaces.getName()
                print("\t\t地点：%s" % uniquePlaceName, end='')
            elif isinstance(uniquePlaces, list):
                for uniquePlace in uniquePlaces:
                    uniquePlaceName = uniquePlace.getName()
                    print("\t\t地点：%s" % uniquePlaceName, end='')

        print("")
