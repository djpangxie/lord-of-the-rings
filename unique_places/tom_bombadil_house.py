#!/usr/bin/python

from items.unique_items import theOneRing
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

        # 生成战利品
        weapon = Weapon("刺叮", "精灵语：刚多林制造", 2, 22, 8)
        self._sting = weapon
        potion = Potion("森林滋补品", "含有稀有草药", 1, 4, 6)
        self._gift = [potion, potion, potion, potion]

    def enter(self, player):
        """
        允许用户与汤姆·邦巴迪尔对话并获得礼物。

        @param player:  当前玩家
        """
        print(self._greetings)

        print("“我是汤姆·邦巴迪尔。我的妻子金莓和我住在这些森林里。”")
        input("按回车键继续。")
        print("")

        if self._sting is not None and player.getInventory().containsItem(theOneRing):
            print("“我看得出来，你正在进行一次长途旅行，并且携带着一件非常重要的东西。\n我想给你留一份礼物，如果你愿意接受的话。”")
            input("按回车键继续。")
            print("")

            if player.addToInventory(self._sting):
                self._sting = None
            else:
                print("无法接收赠礼。")

        print("“感谢你到森林里来拜访我。”")

        # 给玩家战利品
        if self._gift:
            if player.addToInventory(self._gift[0]):
                del self._gift[0]
            else:
                print("无法接收赠礼。")
