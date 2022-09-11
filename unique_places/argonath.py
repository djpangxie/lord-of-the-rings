#!/usr/bin/python

import constants
from unique_place import UniquePlace


class Argonath(UniquePlace):
    """
    阿刚那斯是安都因河中的独特地点。
    阿刚那斯由“两根巨大的石柱”组成，它们“庞大的灰色身影”“威势逼人”。

    如果玩家访问阿刚那斯，他会被治愈并获得经验。
    """

    def __init__(self, name, description, greetings):
        """
        初始化阿刚那斯。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)

        # 最多获得的经验值
        self._exp = 500

    def enter(self, player):
        """
        阿刚那斯的动作序列。

        @param player:  玩家对象
        """
        # 创建奖励
        name = player.getName()
        maxHp = player.getTotalMaxHp()
        playerExperience = player.getExperience()
        experienceIncrease = int(playerExperience * constants.ARGONATH_EXP_INCREASE)
        if experienceIncrease <= self._exp:
            self._exp -= experienceIncrease
        else:
            experienceIncrease = self._exp
            self._exp = 0

        # 剧情
        print(self._greetings)
        print("")
        print("当你凝视古时的国王时，你想到现今的时代和它目前的黑暗。")
        input("按回车键继续。")
        print("")

        # 玩家获得奖励
        print("你在自己内心深处积蓄着力量，以坚定前往魔多完成任务的决心！")

        if experienceIncrease:
            print("\n%s 获得 %s 经验值。\n" % (name, experienceIncrease))
            player.increaseExperience(experienceIncrease)

        player.heal(maxHp)

        input("按回车键继续。")
        print("")
