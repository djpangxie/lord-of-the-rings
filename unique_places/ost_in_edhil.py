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
        Enter Ost-in-Edhil.

        @param player:  The current player.
        """
        healing = player.getMaxHp() - player.getHp()
        
        print(self._greetings)
        print("")
        print("You decide that this is a good place to spend the night.")
        input("Press enter to continue. ")
        print("")
            
        player.heal(healing)
        print("%s was healed by %s!" % (player.getName(), healing))
        print("")

        print("You awaken refreshed and ready for a new day.")
        print("")