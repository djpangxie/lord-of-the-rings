#!/usr/bin/python

from place import Place
from cities.building import Building


class City(Place):
    """
    城市派生自Place。
    城市作为游戏的城镇。城市可能有旅馆、商店和广场。
    """

    def __init__(self, name, description, greetings, buildings=None):
        """
        初始化城市。

        @param name:           城市名称
        @param description:    城市的描述
        @param greetings:      玩家进入该城市时得到的问候
        @param buildings:      城市中所有建筑物对象的列表
        """
        Place.__init__(self, name, description, greetings)

        self._buildings = buildings

    def getGreetings(self):
        """
        返回玩家进入城市时得到的问候。

        @return:    玩家进入城市时得到的问候
        """
        return self._greetings

    def getBuildings(self):
        """
        返回城市中所有建筑物对象的列表。

        @return:    城市中所有建筑物对象的列表
        """
        return self._buildings

    def getBuildingString(self, string):
        """
        返回与城市中建筑物名称相匹配的建筑对象。

        @param string:    建筑物的名称
        
        @return:          如果找到，则为该建筑对象，否则为None
        """
        for building in self._buildings:
            if building.getName() == string:
                return building
        else:
            return None

    def _printBuildings(self):
        """
        打印城市中包含的建筑物并创建包含这些建筑的列表。
        """
        table = []
        buildings = self.getBuildings()
        # 如果只有一个建筑
        if isinstance(buildings, Building):
            print("\t%d.%s" % (1, buildings.getName()))
            table.append(buildings)
        # 如果有多个建筑物
        elif isinstance(buildings, list):
            for num, building in enumerate(buildings, 1):
                print("\t%d.%s" % (num, building.getName()))
                table.append(building)
        print("")
        return table

    def enter(self, player):
        """
        城市的动作序列。

        @param player:       玩家对象
        """
        print("你进入了%s：" % self.getName(), end='')
        print("%s" % self.getDescription())
        print("\n%s\n" % self.getGreetings())
        input("按回车键继续。")
        print("")

        while True:
            print("这里有下列去处：")

            # 打印建筑物清单
            print("\t0.离开")
            table = self._printBuildings()

            # 用户输入
            while True:
                try:
                    choice = input("输入去处的整数序号值：")
                    choice = int(choice)
                except ValueError:
                    choice = -1
                if 0 <= choice <= len(table):
                    break
                else:
                    print("去处序号输入有误！")

            # 如果玩家选择离开城市
            if choice == 0:
                print("\n你离开了%s" % self.getName())
                return

            # 进入建筑
            table[choice - 1].enter(player)

            # 提示下一步操作
            print("\n你回到了%s：%s\n" % (self.getName(), self.getDescription()))
