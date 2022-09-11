#!/usr/bin/python

import random

import battle_engine
import constants
from cities.city import City
from unique_place import UniquePlace
from .command import Command


class EnterCommand(Command):
    """
    使玩家进入城市或独特地点。
    """

    def __init__(self, name, explanation, player):
        """
        初始化进入命令。

        @param name:         命令名称
        @param explanation:  命令的说明
        @param player:       玩家对象
        """
        Command.__init__(self, name, explanation, time=False)

        self._player = player

    def _displayPlacesToEnter(self):
        """
        显示玩家可以进入的地点（城市或独特地点），并创建地区内地点的列表。
        """
        playerName = self._player.getName()
        space = self._player.getLocation()
        city = space.getCity()
        uniquePlace = space.getUniquePlace()

        # 打印可能进入的地方，并录入列表
        print("%s 可以进入下列地点：" % playerName)
        table = []
        num = 1
        if isinstance(city, City):
            print("\t%d.%s" % (num, city.getName()))
            table.append(city)
            num += 1
        elif isinstance(city, list):
            for num, eachCity in enumerate(city, 1):
                print("\t%d.%s" % (num, eachCity.getName()))
                table.append(eachCity)
            num += 1
        if isinstance(uniquePlace, UniquePlace):
            print("\t%d.%s" % (num, uniquePlace.getName()))
            table.append(uniquePlace)
        elif isinstance(uniquePlace, list):
            for number, eachUniquePlace in enumerate(uniquePlace, num):
                print("\t%d.%s" % (number, eachUniquePlace.getName()))
                table.append(eachUniquePlace)
        print("")
        return table

    def execute(self):
        """
        允许玩家进入城市或独特地点。
        """
        space = self._player.getLocation()
        city = space.getCity()
        uniquePlace = space.getUniquePlace()

        # 如果没有地点可以进入
        if not (city or uniquePlace):
            print("地区中没有可探索的地点。")
            return

        # 显示玩家可以进入的地方，并创建地区内地点的列表
        table = self._displayPlacesToEnter()

        # 用户输入
        while True:
            try:
                choice = input("输入地点的整数序号值：")
                choice = int(choice)
            except ValueError:
                choice = -1
            if 1 <= choice <= len(table):
                break
            else:
                print("地点序号输入有误！")

        self._battlePhase()
        table[choice - 1].enter(self._player)

    def _battlePhase(self):
        """
        评估是否会发生随机战斗。如果是的话，将调用battle_engine.battle()来执行战斗。
        """
        currentLocation = self._player.getLocation()
        battleProbability = currentLocation.getBattleProbability()

        # 确定是否会发生随机战斗
        if random.random() < battleProbability:
            # 发生战斗，结束战斗
            battle_engine.battle(self._player, constants.BattleEngineContext.RANDOM)
