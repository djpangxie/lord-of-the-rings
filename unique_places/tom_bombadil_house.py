#!/usr/bin/python

from unique_place import UniquePlace
from items.weapon import Weapon
from items.potion import Potion

class TomBombadilHouse(UniquePlace):
    """
    汤姆·邦巴迪尔的家是一所位于老林子中的独特地点
    在托尔金的宇宙中，汤姆·邦巴迪尔是一个隐秘的神秘主义者，他的身份和目的从未被完全解释过。
    如果玩家拜访汤姆·邦巴迪尔，他就有机会对话并获得一些物品。
    """
    def __init__(self, name, description, greetings):
        """
        初始化汤姆·邦巴迪尔的家
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)
        
        #生成战利品
        description = "有一个秘密的锋利的刀口"
        weapon = Weapon("短杖", description, 4, 2, 2)
        description = "含有稀有草药"
        potion = Potion("森林滋补品", description, 1, 4, 6)
        self._gift = [weapon, potion]
        
    def enter(self, player):
        """
        允许用户与汤姆·邦巴迪尔对话并获得礼物。

        @param player:  当前玩家
        """
        #Story
        print(self._greetings)
        
        print ("\"I am Tom Bombadil. My wife Goldberry and I live in these"
            " forests.\"")
        input("Press enter to continue. ")
        print("")
        
        print ("\"I can tell that you are on a long journey and are carrying"
            " something that \nmust be kept safe. I would like to leave you with"
            " a gift if you would like to \naccept it.\"")
        input("Press enter to continue. ")
        print("")
        
        #Give player loot
        for item in self._gift:
            if player.addToInventory(item):
                self._gift.remove(item)
        input("Press enter to continue. ")
        print("")
        
        print("\"Thank you for visiting me in these forests.\"")