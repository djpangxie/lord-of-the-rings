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

    def _createDictionaryOfBuildings(self):
        """
        Creates a dictionary of building objects. Name-pairs are 
        building names and the objects they correspond to.
        
        @return:    A dictionary of buildings name and their 
                    corresponding objects.
        """
        buildingDictionary = {}
        buildings = self.getBuildings()
        # If there is one building
        if isinstance(buildings, Building):
            buildingDictionary[buildings.getName()] = buildings
        # If there are multiple buildings
        elif isinstance(buildings, list):
            for building in buildings:
                buildingDictionary[building.getName()] = building

        return buildingDictionary

    def _printBuildings(self):
        """
        Helper method that prints the building contained in city.
        """
        buildings = self.getBuildings()
        # If there is one building
        if isinstance(buildings, Building):
            print("\t%s" % buildings.getName())
        # If there are multiple buildings
        elif isinstance(buildings, list):
            for building in buildings:
                print("\t%s" % building.getName())
        print("")

    def enter(self, player):
        """
        The action sequence for city.

        @param player:       The current player
        """
        buildingDictionary = self._createDictionaryOfBuildings()

        print("Entering %s!" % self.getName())
        print("%s" % self.getDescription())
        print("%s" % self.getGreetings())
        input("Press enter to continue. ")
        print("")

        while True:
            print("You have found the following:")

            # Print list of buildings
            self._printBuildings()

            print("To go to a building type its name. Otherwise, type 'leave'")
            command = input("Where would you like to go?\n")

            # If player chooses to leave the city
            if command == 'leave':
                print("")
                print("Leaving %s." % self.getName())
                return

            # For other choices
            if command in list(buildingDictionary.keys()):

                # Enter building
                buildingDictionary[command].enter(player)

                # Prompt for next action
                print("\nYou are now back in %s." % self.getName())
                print("")
            else:
                print("\nI did not recognize %s. Try again.\n" % command)
