#!/usr/bin/python

from .command import Command
from space import Space
from player import Player
from cities.city import City
from unique_place import UniquePlace


class DescribeCommand(Command):
    """
    向用户描述当前所在地区。
    """

    def __init__(self, name, explanation, player):
        """
        初始化新的描述命令。

        @param name:         命令名称
        @param explanation:  命令的说明
        @param player:       玩家对象
        """
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        命令执行。
        """
        # 创建变量
        location = self._player.getLocation()
        locationName = location.getName()
        locationDescription = location.getDescription()
        items = location.getItems()
        itemsList = items.getItems()
        city = location.getCity()
        uniquePlace = location.getUniquePlace()

        # 打印地区名称和描述
        print("%s：%s" % (locationName, locationDescription))

        # 如果地区中没有城市或独特地点
        if not city and not uniquePlace:
            print("%s中没有地点可供探索。" % locationName)

        # 如果至少有一个城市或独特地点
        else:
            print("%s中存在下列地点：" % locationName)

            # 如果地区中有一个城市：
            if isinstance(city, City):
                cityName = city.getName()
                print("\t%s：%s" % (cityName, city.getDescription()))

            # 如果地区中有多个城市：
            elif isinstance(city, list):
                for eachCity in city:
                    eachCityName = eachCity.getName()
                    print("\t%s：%s" % (eachCityName, eachCity.getDescription()))

            # 如果地区中有一个独特地点
            if isinstance(uniquePlace, UniquePlace):
                uniquePlaceName = uniquePlace.getName()
                print("\t%s：%s" % (uniquePlaceName, uniquePlace.getDescription()))

            # 如果地区中有多个独特地点
            if isinstance(uniquePlace, list):
                for eachUniquePlace in uniquePlace:
                    eachUniquePlaceName = eachUniquePlace.getName()
                    print("\t%s：%s" % (eachUniquePlaceName, eachUniquePlace.getDescription()))

        # 如果地区中含有物品
        if itemsList:
            print("%s中存在下列物品：" % locationName)
            for item in itemsList:
                print("\t%s" % item.getName())
