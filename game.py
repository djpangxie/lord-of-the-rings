#!/usr/bin/python

import random
import sys

import game_loader
import battle_engine
from parser import Parser
from commands.north_command import NorthCommand
from commands.south_command import SouthCommand
from commands.east_command import EastCommand
from commands.west_command import WestCommand
from commands.enter_command import EnterCommand
from items.unique_items import theOneRing
import constants


class Game(object):
    """
    准备并执行回合制游戏。
    """

    def __init__(self):
        """
        初始化游戏。
        """
        print("...游戏加载中...")
        print("...")

        # 初始化游戏对象
        self._world = game_loader.getWorld()
        self._shire = self._world[0]
        self._orodruin = self._world[26]

        startingInventory = game_loader.getStartingInventory()
        self._player = game_loader.getPlayer(self._shire, startingInventory)
        self._commandList = game_loader.getCommandList(self._player)

        print("...")
        print("$$$加载完毕$$$")

        # 创建解析器
        self._parser = Parser(self._commandList)

    def play(self):
        """
        执行游戏主循环。
        """
        splashScreen = """
        """
        print(splashScreen)
        print("这是一款冒险游戏，你需要为你的英雄收集各种装备以对抗魔多。")
        print("一路走来，亲爱的小拉德、迈尔斯、塞思和C-$提供了一点帮助。")
        print("...~Money~...")
        print("")
        print("(键入'help'来显示一个可用的命令列表)")
        print("")

        while (True):
            self._nextTurn()

    def _nextTurn(self):
        """
        从玩家那里获得下一个命令。如果nextCommand被成功执行，并且涉及到时间的流逝，那么在nextCommand被执行之后，有可能会发生一场随机的战斗。
        有可能执行失败的指令：四个移动命令。
        """
        # 执行下一个命令
        nextCommand = self._parser.getNextCommand()

        if nextCommand is not None:
            # 检查命令的执行情况
            if self._executionCheck(nextCommand):
                # 然后执行NextCommand
                nextCommand.execute()
                # 如果时间流逝......有可能发生随机的战斗
                if nextCommand.getTime():
                    self._battlePhase()
            print("")

        else:
            errorMsg = "从解析器接收命令失败。"
            raise AssertionError(errorMsg)

        # 如果玩家已经赢得了游戏
        if self._winningConditions():
            print(("尊敬的%s，恭喜你拯救了中土世界！" % self._player.getName()))
            input("按下回车键退出。")
            sys.exit()

    def _executionCheck(self, nextCommand):
        """
        检查用户的命令是否可以被执行。这只适用于四个移动命令。
        这个方法是为了防止在不能执行命令的情况下发生随机战斗。

        @return:              如果命令将被成功执行，则为"True"，否则为"False"
        """
        space = self._player.getLocation()

        # 检查移动指令
        if isinstance(nextCommand, NorthCommand):
            if not self._player.canMoveNorth():
                print("无法向北移动。")
                return False
        elif isinstance(nextCommand, SouthCommand):
            if not self._player.canMoveSouth():
                print("无法向南移动。")
                return False
        elif isinstance(nextCommand, EastCommand):
            if not self._player.canMoveEast():
                print("无法向东移动。")
                return False
        elif isinstance(nextCommand, WestCommand):
            if not self._player.canMoveWest():
                print("无法向西移动。")
                return False

        return True

    def _battlePhase(self):
        """
        评估是否会发生随机战斗。如果是的话，将调用battle_engine.battle()来执行战斗。
        """
        currentLocation = self._player.getLocation()
        battleProbability = currentLocation.getBattleProbability()

        # 确定是否会发生随机战斗
        if random.random() < battleProbability:
            # 呼唤战斗，解决战斗
            battle_engine.battle(self._player, constants.BattleEngineContext.RANDOM)

    def _winningConditions(self):
        """
        评估玩家是否已经赢得游戏。赢得游戏的标准是至尊魔戒被丢在欧洛都因（末日火山）地区。
        """
        if self._orodruin.containsItem(theOneRing):
            return True
        else:
            return False
