#!/usr/bin/python

from .command import Command


class UnequipCommand(Command):
    """
    卸下玩家当前装备的物品。
    """

    def __init__(self, name, explanation, player):
        """
        初始化卸下命令。

        @param name:         命令名称
        @param explanation:  命令的说明
        @param player:       玩家对象
        """
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        使玩家卸下装备栏中装备的物品。
        """
        equipped = self._player.getEquipped()

        # 如果没有装备任何物品
        if equipped.count() == 0:
            print("没有装备任何物品。")
            return

        # 用户输入
        print("%s 可以卸下：" % self._player.getName())
        for num, item in enumerate(equipped, 1):
            print("\t%d.%s" % (num, item.getName()))
        print("")

        while True:
            try:
                choice = input("输入装备的整数序号值：")
                choice = int(choice)
            except ValueError:
                choice = -1
            if 1 <= choice <= equipped.count():
                break
            else:
                print("装备序号输入有误！")

        # 卸下装备
        statement = self._player.unequip(equipped.getItems()[choice - 1])
        print(statement)
