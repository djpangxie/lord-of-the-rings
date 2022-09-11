#!/usr/bin/python

import random

import battle_engine
import constants
from .command import Command


class PickUpCommand(Command):
    """
    使玩家从其当前地区中拾取物品。
    """

    def __init__(self, name, explanation, player):
        """
        初始化拾取命令。

        @param name:         命令名称
        @param explanation:  命令的说明
        @param player:       玩家对象
        """
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        从地区中拾取物品并将其添加到库存中。
        """
        name = self._player.getName()
        location = self._player.getLocation()
        locationItems = location.getItems()

        # 如果没有可供拾取的物品
        if locationItems.count() == 0:
            print("地区中没有可拾取的物品。")
            return

        # 用户输入
        print("%s 可以拾取：" % name)
        for num, item in enumerate(locationItems, 1):
            print("\t%d.%s" % (num, item.getName()))
        print("")

        while True:
            try:
                choice = input("输入物品的整数序号值：")
                choice = int(choice)
            except ValueError:
                choice = -1
            if 1 <= choice <= locationItems.count():
                break
            else:
                print("物品序号输入有误！")

        # 拾取物品
        result = self._battlePhase()
        if result:
            if self._player.addToInventory(locationItems.getItems()[choice - 1]):
                location.removeItem(locationItems.getItems()[choice - 1])
        else:
            bonusDifficulty = location.getBattleBonusDifficulty()
            if bonusDifficulty > 0 and random.random() < bonusDifficulty:
                location.removeItem(locationItems.getItems()[choice - 1])
            elif bonusDifficulty < 0 and random.random() < -bonusDifficulty:
                if self._player.addToInventory(locationItems.getItems()[choice - 1]):
                    location.removeItem(locationItems.getItems()[choice - 1])

    def _battlePhase(self):
        """
        评估是否会发生随机战斗。如果是的话，将调用battle_engine.battle()来执行战斗，并返回战斗结果。
        """
        currentLocation = self._player.getLocation()
        battleProbability = currentLocation.getBattleProbability()

        # 确定是否会发生随机战斗
        if random.random() < battleProbability:
            # 发生战斗，结束战斗，返回战斗结果
            return battle_engine.battle(self._player, constants.BattleEngineContext.RANDOM)
        else:
            # 没有发生战斗，战斗结果也算作赢了
            return True
