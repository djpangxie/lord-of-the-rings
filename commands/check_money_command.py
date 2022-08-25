#!/usr/bin/python

from .command import Command
import constants

class CheckMoneyCommand(Command):
    """
    显示玩家金钱。
    """
    def __init__(self, name, explanation, player):
        """
        初始化新的检查金钱命令。

        @param name:         命令名称
        @param explanation:  命令的说明
        @param player:       玩家对象
        """
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Prints player money.
        """
        money = self._player.getMoney()
        name = self._player.getName()

        print("%s currently has %s %s!" % (name, money, constants.CURRENCY))