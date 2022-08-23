#!/usr/bin/python

from unique_place import UniquePlace
from monsters.nazgul_ii import Nazgul_II
from monsters.orc import Orc
from monsters.orc_archer import OrcArcher
from monsters.troll import Troll
from monsters.black_numernorian import BlackNumernorian
from monsters.witch_king import WitchKing
from battle_engine import battle
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.item import Item
import constants

import random

class DolGuldur(UniquePlace):
    """
    多古尔都是黑森林南部的一个独特地点，其名称的意思是“妖术之山”。
    如果玩家访问多古尔都，他有机会与一些困难的怪物战斗并获得一些战利品。
    """
    def __init__(self, name, description, greetings):
        """
        初始化多古尔都。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)
        
        self._wave = []
        self._wave2 = []
        self._wave3 = []
        
        #创造第一波怪物
        for monster in range(11):
            monster = Orc(constants.MONSTER_STATS[Orc])
            self._wave.append(monster)
        for monster in range(10):
            monster = OrcArcher(constants.MONSTER_STATS[OrcArcher])
            self._wave.append(monster)
        for monster in range(7):
            monster = Troll(constants.MONSTER_STATS[Troll])
            self._wave.append(monster)
        
        #创造第二波怪物
        numberNazgul = random.randrange(0, 8)
        for monster in range(numberNazgul):
            nazgul = Nazgul_II(constants.MONSTER_STATS[Nazgul_II])
            self._wave2.append(nazgul)
        if random.random() < constants.DOL_GULDUR_WITCH_KING_PROB:
            witchKing = WitchKing(constants.MONSTER_STATS[WitchKing])
            self._wave2.append(witchKing)
        for monster in range(8):
            monster = BlackNumernorian(constants.MONSTER_STATS[BlackNumernorian])
            self._wave2.append(monster)
            
        #创造第三波怪物
        numberNazgul = random.randrange(0, 8)
        for monster in range(numberNazgul):
            nazgul = Nazgul_II(constants.MONSTER_STATS[Nazgul_II])
            self._wave3.append(nazgul)
        for monster in range(6):
            monster = BlackNumernorian(constants.MONSTER_STATS[BlackNumernorian])
            self._wave3.append(monster)

        # self._wave3.append(monster)

        #生成战利品
        weapon = Weapon("诅咒之剑", "使你充满恐惧", 5, 18, 18)
        weapon2 = Weapon("诅咒之斧", "你光拿着就已经失去了获胜的信心", 5, 22, 16)
        armor = Armor("诅咒之盾", "其上布满了千疮百孔", 5, 12, 1)
        potion = Potion("诅咒药剂", "一种不明物质", 2, 0, -10)
        item = Item("被诅咒的镜子", "只见奇怪的扭曲和阴影", 6, 18)
        item2 = Item("被诅咒的书籍", "魔典", 4, 72)
        self._loot = [weapon, weapon2, armor, potion, item, item2]
        
    def enter(self, player):
        """
        The action sequence for Dol Guldur.
        
        @param player:   The current player.
        """
        print(self._greetings)
        print("")
        
        #Solicit user choice
        choice = self._choice()
        
        #Carry out action sequence given user choice
        if choice == "frontal assault":
            self._frontalAssault(player)
        if choice == "escape":
            self._run(player)
            
    def _choice(self):
        """
        Solicit user choice. Here, user is given option to attack or to run. 
        """
        choice = None
        acceptable = ["frontal assault", "escape"]
        while choice not in acceptable:
            choice = input("What do you want to do? Choices: 'frontal" 
                " assault' or 'escape.' ")
        print("")
        
        return choice
        
    def _frontalAssault(self, player):
        """
        Action sequence for frontal assault option.
        
        @param player:   The current player.
        """
        #Monster battles
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave)
        if not result:
            return
            
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave2)
        if not result:
            return
            
        #Call _victorySequence
        self._victorySequence(player)
        
    def _victorySequence(self, player):
        """
        Victory sequence for taking Dol Guldur.
        
        @param player:   The current player.
        """
        #Story
        print ("Although you have taken the tower of Dol Guldur, a deep sense" 
            " of evil still \nlingers over the land.")
        input("Press enter to continue. ")
        print("")
        
        #Give player loot
        if len(self._loot) != 0:
            print("While looking around, you find several items.")
            input("Press enter to continue. ")
            print("")
            for item in self._loot:
                if player.addToInventory(item):
                    self._loot.remove(item)
            print("")
        
        #Story
        print("You leave with a sense of foreboding.")
        print("")
        
    def _run(self, player):
        """
        Action sequence for run option.
        
        @param player:   The current player.
        """
        print("You find yourself surrounded.")
        input("Press enter to continue. ")
        print("")
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave3)
        if not result:
            return
        
        print("You escape with your life!")
        print("")