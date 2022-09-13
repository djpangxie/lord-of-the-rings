#!/usr/bin/python
import random

import constants
from items.potion import Potion
from unique_place import UniquePlace


class Derningle(UniquePlace):
    """
    秘林谷是位于范贡森林中的独特地点。

    如果玩家访问秘林谷，他有机会与树须互动，获得物品和经验。
    """

    def __init__(self, name, description, greetings):
        """
        初始化秘林谷。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)

        # 创建礼物
        self._gift = []
        description = "一种恩特用河水酿制的有魔力的饮料。"
        for potion in range(3):
            potion = Potion("恩特饮料", description, 2, 42, 100)
            self._gift.append(potion)

        # 最多获得的经验值
        self._exp = 150

    def enter(self, player):
        """
        进入秘林谷。

        @param player:  玩家对象
        """
        # 剧情
        print(self._greetings)
        print("")
        print("你发现自己在范贡森林的深处，而且周边的树都好似活的一样。")
        input("按回车键继续。")
        print("")

        # 征求用户输入
        print("你来到树林中的一个岔路口。")
        input("按回车键继续。")
        print("")
        self._fork()

        # 随机选择一条目的地
        choice = random.randrange(3)
        if choice == 0:
            self._leftDestination(player)
        elif choice == 1:
            self._straightDestination()
        else:
            self._rightDestination(player)

    def _fork(self):
        """
        请求用户输入。
        """
        choice = None
        acceptable = ["left", "straight", "right"]
        while choice not in acceptable:
            choice = input("你想走哪边？选项：左边(left)、直行(straight)、右边(right) ")
        print("")

    def _leftDestination(self, player):
        """
        得到经验奖励。
        
        @param player:  玩家对象
        """
        # 计算经验增幅数值
        experienceIncrease = int(player.getExperience() * constants.DERINGLE_EXP_INCREASE)
        if experienceIncrease <= self._exp:
            self._exp -= experienceIncrease
        else:
            experienceIncrease = self._exp
            self._exp = 0

        # 剧情
        print("你发现自己来到范贡森林深处的一片洒满阳光的草地上，一时间你竟忘了还身处魔影笼罩的危险之中。")
        input("按回车键继续。")
        print("")

        # 玩家获得经验增长
        if experienceIncrease:
            print("你突然意识到：你不仅仅是在为自己而战，还是在为像这样美丽的地方而战，你的内心瞬间涌现出强大的力量。")
            input("按回车键继续。")
            print("")

            print("%s 获得了 %s 经验。" % (player.getName(), experienceIncrease))
            player.increaseExperience(experienceIncrease)
            input("按回车键继续。")
            print("")
        # 无法再获得经验
        else:
            print("你情不自禁的躺在了草丛之中，任由温暖的阳光照在身上，呼吸着香甜的空气，欣赏着鸟儿动听的歌唱。")
            input("按回车键继续。")
            print("")

            print("有好一会，尘世的喧嚣离你而去，你不再感到任何忧虑，直到最终你恋恋不舍的离开了这里。")
            input("按回车键继续。")
            print("")

    def _straightDestination(self):
        """
        来到被萨茹曼手下的奥克摧残过的森林边缘。
        """
        # 剧情
        print("你来到了一片被滥砍乱伐、光秃秃并被烧焦的树林边缘。")
        input("按回车键继续。")
        print("")

        print("“这铁定是萨茹曼的杰作！”，你内心想着。")
        input("按回车键继续。")
        print("")

        print("瞬间你再无任何心情游荡，于是匆匆离开了。")
        print("")

    def _rightDestination(self, player):
        """
        遇到树须，并收到礼物。

        @param player:  玩家对象
        """
        # 剧情
        print("你发现自己走入一个黑暗的林中通道里，并且听到窸窸窣窣的声响，你感到很不安。")
        input("按回车键继续。")
        print("")

        print("您你鼓起勇气穿了过去，发现自己正处在多名恩特的身边，而他们此时正注视着你！")
        input("按回车键继续。")
        print("")

        print("树须：“你好 %s ！甘道夫跟我说起过你，我们知道你在这儿。”" % player.getName())
        input("按回车键继续。")
        print("")

        print("树须：“不过，这会儿我们正在召开恩特大会呢！请原谅招待不周。”")
        input("按回车键继续。")
        print("")

        print("这时一个看起来较年轻的恩特跑了过来，并带着你前往树林旁边的恩特之家。")
        input("按回车键继续。")
        print("")

        # 玩家收到礼物
        if self._gift:
            print("急楸：“给，这些是树须要我为你准备的礼物！”")
            input("按回车键继续。")
            print("")

            if player.addToInventory(self._gift[0]):
                self._gift.pop(0)
            print("")
        # 礼物给完了
        else:
            print("你和这名恩特边走边聊，并在周边闲逛了好一会，最后你们互相道别。")
            input("按回车键继续。")
            print("")
