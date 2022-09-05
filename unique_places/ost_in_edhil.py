#!/usr/bin/python

from unique_place import UniquePlace


class OstInEdhil(UniquePlace):
    """
    欧斯特-因-埃第尔是安都因河中的独特地点。这里曾经是一座伟大的城市，在索伦摧毁它之前，一直是精灵居住的地方。

    如果玩家访问这里，他将被治愈。
    """

    def __init__(self, name, description, greetings):
        """
        初始化欧斯特-因-埃第尔。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)

    def enter(self, player):
        """
        进入欧斯特-因-埃第尔。

        @param player:  玩家对象
        """
        healing = player.getTotalMaxHp() - player.getHp()

        print(self._greetings)
        print("")
        print("你觉得这是一个过夜的好地方。")
        input("按回车键继续。")
        print("")

        player.heal(healing)
        print("%s 治愈了 %s 点生命值！" % (player.getName(), healing))
        print("")

        print("你醒来时神清气爽，准备迎接新的一天。")
        print("")
