#!/usr/bin/python

import constants
from cities.building import Building


class Inn(Building):
    """
    旅店派生自建筑。
    旅店是允许玩家有偿治疗的建筑地点。
    """

    def __init__(self, name, description, greetings, cost):
        """
        初始化旅店

        @param name:         旅店的名字
        @param description:  旅店的描述
        @param greetings:    玩家进入旅店时得到的问候
        @param cost:         使用旅店的费用
        """
        Building.__init__(self, name, description, greetings)

        self._cost = cost

    def enter(self, player):
        """
        玩家进入旅馆时的动作序列。
        
        @param player:     玩家对象
        """
        cost = self.getCost()

        print("")
        print("- - - %s - - -" % self.getName())
        print(self._greetings)
        print("住宿费用：%s" % cost)

        # 确定玩家选择
        choice = None
        while choice != "no":
            print("")
            choice = input("你想留下来过夜吗？(yes/no): ")

            # 治愈选项
            if choice == "yes":
                # 支付金钱
                if player.getMoney() >= cost:
                    player.decreaseMoney(cost)
                    # 实际治愈玩家
                    self._heal(player)
                    print("%s 花费了 %s%s 在此留宿了一夜！" % (player.getName(), cost, constants.CURRENCY))
                # 没有足够的钱
                else:
                    print("%s 没有足够的金钱。" % player.getName())
                input("按回车键继续。")
                return

            # 不使用选项
            elif choice == "no":
                print("%s欢迎您再次光临！" % self._name)
                input("按回车键继续。")

            # 对于无效输入
            else:
                print("'什么？'")

    def getCost(self):
        """
        返回旅店的费用。
        
        @return:    一个整数值表示的使用旅店的花费
        """
        return self._cost

    def _heal(self, player):
        """
        治愈玩家至最大生命值。

        @param player:    玩家对象
        """
        maxHp = player.getTotalMaxHp()
        hp = player.getHp()
        amountToHeal = maxHp - hp

        player.heal(amountToHeal)
