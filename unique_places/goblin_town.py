#!/usr/bin/python

from unique_place import UniquePlace
from items.weapon import Weapon
from monsters.goblin import Goblin
from monsters.great_goblin import GreatGoblin
from battle_engine import battle
import constants

import random

class GoblinTown(UniquePlace):
    """
    半兽人镇是高隘口中的独特地点。
    
    玩家有机会尝试从半兽人镇周围潜伏过去或直接攻入。
    如果潜伏的尝试不成功，玩家必须同时与大量的怪物作战。
    """
    def __init__(self, name, description, greetings):
        """
        初始化半兽人镇。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)

        #生成战利品
        weapon1 = Weapon("半兽人砍刀", "对精怪有益，对人类有害", 3, 5, 6)
        weapon2 = Weapon("矮人战斧", "从孤山偷来的", 4, 8, 12)
        weapon3 = Weapon("长柄斧", "看起来是从刚铎人那偷来的赃物", 6, 12, 14)
        self._loot = [weapon1, weapon2, weapon3]

        #我们将有四波怪物
        self._wave = []
        self._wave2 = []
        self._wave3 = []

        #创造第一波怪物
        for monster in range(2):
            monster = Goblin(constants.MONSTER_STATS[Goblin])
            self._wave.append(monster)
            
        #创造第二波怪物
        for monster in range(8):
            monster = Goblin(constants.MONSTER_STATS[Goblin])
            self._wave2.append(monster)

        #创造第三波怪物
        for monster in range(4):
            monster = Goblin(constants.MONSTER_STATS[Goblin])
            self._wave3.append(monster)
        monster = GreatGoblin(constants.MONSTER_STATS[GreatGoblin])
        self._wave3.append(monster)
    
        #将前三波合为第四波怪物
        self._wave4 = self._wave + self._wave2 + self._wave3

    def enter(self, player):
        """
        Action sequence for GoblinTown.

        @param player:  The current player.
        """
        print(self._greetings)
        print("")
        
        #Fight wave 1
        print ("As you creep along High Pass hoping to avoid detection, you" 
            " hear some creeping \nin the shadows....")
        input("Press enter to continue. ")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave)
        if not result:
            return
            
        #Story
        print ("You have defeated some unsuspecting goblins! Escaping" 
            " detection now may \nstill be an option!")
        input("Press enter to continue. ")
        print("")
    
        #Solicit user choice
        print ("As you think ahead, you have two options. You may attempt to" 
            " sneak through \nGollum's Cave taking the risk getting trapped " 
            " or go straight into Goblin Town.")
        print("")
        choice = self._choice()

        #Run choice-dependent scripts
        if choice == "cave":
            self._cave(player)
        else:
            self._frontalAssault(player)
        
    def _choice(self):
        """
        Solicit user choice.
        
        @param player:  The current player.
        """
        choice = None
        acceptable = ["cave", "straight"]
        while choice not in acceptable:
            choice = input("What would you like to do? Choices: try to" 
                " sneak through the 'cave' or go 'straight' in. ")
        print("")
        
        return choice
        
    def _cave(self, player):
        """
        Action sequence for Gollum's cave.
        
        @param player:  The current player.
        """
        print("You try to sneak through Gollum's Cave.")
        input("Press enter to continue. ")
        print("")

        #If player ventures through undetected
        if random.random() < constants.GOBLIN_TOWN_EVASION_PROB:
            print("You make it through the mountains safely!")
            input("Press enter to continue. ")
            print("")
            
        #If player gets  trapped in cave.
        else:
            #Story
            print ("Great Goblin: \"You fool... did you really think you could" 
                " make it through my territory \nwithout me knowing?\"")
            input("Press enter to continue. ")
            print("")
            
            #Fight wave 4
            print("Great Goblin: \"Now I will feast on your flesh....\"")
            input("Press enter to continue. ")
            print("")
            result = battle(player, constants.BattleEngineContext.STORY, 
                self._wave4)
            if not result:
                return
            
            #Call victory sequence
            self._victorySequence(player)
            
    def _frontalAssault(self, player):
        """
        Action sequence for frontal assault choice.
        
        @param player:  The current player.
        """
        #Story
        print("Time to slay some goblins! On to Goblin Town!")
        input("Press enter to continue. ")
        print("")
        
        print("You see some primitive huts, all uninhabited.") 
        input("Press enter to continue. ")
        print("")
        
        print("Suddenly, goblins circle you from all directions!")
        input("Press enter to continue. ")
        print("")

        #Frontal assault wave 1
        print ("Great Goblin: \"What makes you think that you can just charge" 
            " into my city?\"")
        input("Press enter to continue. ")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave2)
        if not result:
            return
            
        #Frontal assault wave 2
        print("Great Goblin: \"You stupid fool it is now time to DIE!\" ")
        input("Press enter to continue. ")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave3)
        if not result:
            return
            
        #Call victory sequence
        self._victorySequence(player)
        
    def _victorySequence(self, player):
        """
        Victory sequence for making it through Goblin Town.
        
        @param player:  The current player.
        """
        print ("As you gaze over the corpses of your enemies, you decide that" 
            " it is time to take your winnings and leave.")
        input("Press enter to continue. ")
        print("")

        #Give player items
        for item in self._loot:
            if player.addToInventory(item):
                self._loot.remove(item)
        print("")
        
        self._createPort("south")