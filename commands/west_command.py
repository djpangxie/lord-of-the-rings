#!/usr/bin/python

from .command import Command


class WestCommand(Command):
    """
    向西命令。
    """

    def __init__(self, name, explanation, player):
        """
        初始化向西命令。

        @param name:            命令名称
        @param explanation:     命令的说明
        @param player:          玩家对象
        """
        Command.__init__(self, name, explanation, time=True)

        self._player = player

    def execute(self):
        """
        运行向西命令。
        """
        # 确保出口存在
        if not self._player.canMoveWest():
            print("无法向西旅行！")
            return

        # 如果玩家将要通过墨瑞亚
        if self._player.getLocation().getName() == "罗瑞恩":
            self._player.moveWest()
            result = self._player.getLocation().getUniquePlace().through(self._player)
            if not result:
                self._player.moveEast()
                return
        # 否则打印用户图形并进行普通旅行
        else:
            print("--------------------------------")
            print("           向西旅行")
            print("      <-----------------        ")
            print("")
            print("--------------------------------")

            # 实际执行移动并打印地区信息
            self._player.moveWest()
        space = self._player.getLocation()
        name = space.getName()
        description = space.getDescription()

        print("你来到了 %s" % name)
        print(description)
