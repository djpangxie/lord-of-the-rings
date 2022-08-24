#!/usr/bin/python

from unique_place import UniquePlace
from monsters.nazgul_ii import Nazgul_II
from battle_engine import battle
from items.weapon import Weapon
from items.armor import Armor
from items.item import Item
import constants
import random

class Tharbad(UniquePlace):
    """
    沙巴德是米斯艾塞尔河中的独特地点。这是一座曾经有人居住的城市的遗迹。
    
    在这里，玩家可以选择探索废墟，探索废墟将使玩家能够冒着与戒灵遭遇的风险搜罗物品。
    """
    def __init__(self, name, description, greetings):
        """
        初始化沙巴德。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)

        #生成玩家可以战斗的戒灵的列表
        self._monsters = []
        numberNazgul = random.randrange(1, 5)
        for monster in range(numberNazgul):
            nazgul = Nazgul_II(constants.MONSTER_STATS[Nazgul_II])
            self._monsters.append(nazgul)

        #生成战利品
        description = "记载着古代的文字与符号"
        scroll = Item("古代卷轴", description, 1, 32)
        description = "看起来它随时都有可能断裂"
        weapon = Weapon("腐烂的法杖", description, 6, 3, 4)
        description = "也许被击打一两次就碎了"
        armor = Armor("腐烂的盾牌", description, 4, 2, 1)
        self._loot = [scroll, weapon, armor]
        
    def enter(self, player):
        """
        Enter Tharbad.

        @param player:  The current player.
        """
        #Story
        print(self._greetings)
        print("")
        
        print ("You gaze upon the ancient ruins of the once great city of" 
            " Tharbad and see some very strange sights.")
        input("Press enter to continue. ")
        print("")

        #Solicit user input
        choice = None
        acceptable = ["explore", "leave"]
        while choice not in acceptable:
            choice = input("What would you like to do? Choices: 'explore'"
                " and 'leave.' ")
            print("")
        
        #Execute user-dependent scripts
        if choice == "explore":
            self._explore(player)
        else:
            print ("You bid farewell to the ruins of Tharbad and continue on" 
                " your journey.")
            print("")

    def _explore(self, player):
        """
        Action sequence for exploring Tharbad.

        @param player:   The player object.
        """
        #Solicit user input
        choice = None
        acceptable = ["ruined mill", "ancient bridge"]
        while choice not in acceptable:
            choice = input("Where would you like to explore? Options:"
                " 'ruined mill' and 'ancient bridge.' ")
        print("")

        #If user chooses to explore ruined mill
        if choice == "ruined mill":
            print ("You find lots of rotting instruments and the remains of"
                " farming equipment.")
            input("Press enter to continue. ")
            print("")
            self._itemFind(player)
            self._chanceBattle(player)

        #If user choose to explore ancient bridge
        elif choice == "ancient bridge":
            print ("You find the ruins of the ancient North-South Road bridge"
                " crossing. This was \nonce one of the greatest causeways in all"
                " of Middle Earth.")
            input("Press enter to continue. ")
            print("")
            self._itemFind(player)
            self._chanceBattle(player)

        #Give player option to keep exploring
        choice = None
        acceptable = ["yes", "no"]
        while choice not in acceptable:
            choice = input("Would you like to keep exploring? Options:"
                " 'yes' and 'no.' ")
        print("")
        
        if choice == "yes":
            self._explore(player)
        else:
            print("You leave Tharbad with a sense of loss.")
            print("")
            
    def _chanceBattle(self, player):
        """
        Determines if a random battle is to occur.
        
        @param player:   The player object.
        """
        if random.random() < constants.THARBAD_BATTLE_PROB and self._monsters:
            print("You hear some rustling in the shadows....")
            input("Press enter to continue. ")
            print("")
            result = battle(player, constants.BattleEngineContext.STORY, 
                self._monsters)
            if not result:
                return
            
    def _itemFind(self, player):
        """
        Determines if player finds an item and then gives player that item.
        
        @param player:   The player object.
        """
        #If there are no items to find
        if len(self._loot) == 0:
            return
        
        chance = random.random()
        #Determines if player finds item and which item player receives
        if chance < constants.THARBAD_ITEM_FIND_PROB:
            print("You find something that may be of some value!")
            item = random.choice(self._loot)
            if player.addToInventory(item):
                self._loot.remove(item)
            print("")