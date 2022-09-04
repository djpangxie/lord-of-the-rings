#!/usr/bin/python

from cities.building import Building
from items.item import Item


class Square(Building):
    """
    广场派生于建筑，并位于城市之中。
    广场作为公共空间，让玩家可以与城里人交流。
    """

    def __init__(self, name, description, greetings, talk=None, items=None):
        """
        初始化广场对象。

        @param name:           广场名称
        @param description:    广场的描述
        @param greetings:      玩家进入广场时得到的问候
        @param talk:           用于对话的 人名-对话 的字典
        @param items:          玩家与人交谈可能会收到的物品
        """
        Building.__init__(self, name, description, greetings)

        self._talk = talk
        self._items = items

    def enter(self, player):
        """
        广场的动作序列。
        
        @param player:     玩家对象
        """
        print("")
        print("- - - %s - - -" % self._name)
        print(self._greetings)
        print("")

        # 如果广场上一个人都没有
        if self._talk == None:
            print("你发现 %s 完全空无一人。" % self._name)
            return

        # 用户输入
        print("在 %s 中有 %d 人可以交谈：" % (self._name, len(self._talk)))
        for num, person in enumerate(self._talk, 1):
            print("\t%d.%s" % (num, person))
        print("\t0.返回")

        while True:
            try:
                choice = input("输入人物的整数序号值：")
                choice = int(choice)
            except ValueError:
                choice = -1
            if 1 <= choice <= len(self._talk):
                table = list(self._talk.items())[choice - 1]
                print("\n{:s}：“{:s}”\n".format(*table))
                # 如果该人物会送你物品
                if table[0] in self._items:
                    self._giveItem(player, table[0])
            elif choice == 0:
                return
            else:
                print("人物序号输入有误！")

    def _giveItem(self, player, name):
        """
        负责处理玩家接收物品的辅助方法。
        
        @param player:    玩家对象
        @param name:      用户选择与之交谈的人物的名字
        """
        gift = self._items[name]

        # 如果礼物是单个物品
        if isinstance(gift, Item):
            if player.addToInventory(gift):
                print("%s 将 %s 赠与了 %s" % (name, gift.getName(), player.getName()))
                del self._items[name]
            else:
                print("无法接收赠礼。")

        # 如果礼物是包含多个物品的列表
        elif isinstance(gift, list):
            while gift:
                if player.addToInventory(gift[0]):
                    print("%s 将 %s 赠与了 %s" % (name, gift[0].getName(), player.getName()))
                    del gift[0]
                else:
                    print("无法接收赠礼。")
                    return

            del self._items[name]
