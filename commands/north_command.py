#!/usr/bin/python

from .command import Command


class NorthCommand(Command):
    """
    向北命令。
    """

    def __init__(self, name, explanation, player):
        """
        初始化向北命令。

        @param name:            命令名称
        @param explanation:     命令的说明
        @param player:          玩家对象
        """
        Command.__init__(self, name, explanation, time=True)

        self._player = player

    def execute(self):
        """
        运行向北命令。
        """
        # 确保出口存在
        if not self._player.canMoveNorth():
            print("无法向北旅行！")
            return

        # 用户图形
        print("--------------------------------")
        print("           向北旅行")
        print("              /\                ")
        print("              ||                ")
        print("              ||                ")
        print("")

        # 实际执行移动并打印地区信息
        self._player.moveNorth()

        space = self._player.getLocation()
        name = space.getName()
        description = space.getDescription()

        print("你来到了 %s" % name)
        print(description)
