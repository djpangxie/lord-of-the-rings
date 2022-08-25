#!/usr/bin/python

from unique_place import UniquePlace
from monsters.uruk_hai import UrukHai
from monsters.uruk_hai_archer import UrukHaiArcher
from monsters.elite_uruk_hai import EliteUrukHai
from monsters.sauroman import Sauroman
from battle_engine import battle
from items.item import Item
import constants

class Isenguard(UniquePlace):
    """
    艾森加德是位于卡伦纳松的独特地点。它是萨鲁曼的要塞和基地。
    
    如果玩家访问艾森加德，他就有机会与一波又一波的敌人战斗，并获得一些战利品。
    """
    def __init__(self, name, description, greetings):
        """
        初始化艾森加德。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)

        #这里有三波怪物
        self._wave = []
        self._wave2 = []
        self._wave3 = []

        #创建第一波怪物
        for monster in range(6):
            urukHai = UrukHai(constants.MONSTER_STATS[UrukHai])
            self._wave.append(urukHai)
        for monster in range(3):
            urukHaiArcher = UrukHaiArcher(constants.MONSTER_STATS[UrukHaiArcher])
            self._wave.append(urukHaiArcher)
        
        #创建第二波怪物
        for monster in range(10):
            eliteUrukHai = EliteUrukHai(constants.MONSTER_STATS[EliteUrukHai])
            self._wave2.append(eliteUrukHai)
        for monster in range(4):
            urukHaiArcher = UrukHaiArcher(constants.MONSTER_STATS[UrukHaiArcher])
            self._wave2.append(urukHaiArcher)

        #创建第三波怪物 - 乌鲁克族精英的基础数据翻倍了
        BONUS = 3
        increasedStats = []
        for stat in constants.MONSTER_STATS[EliteUrukHai]:
            increasedStats.append(stat * BONUS)
        for monster in range(2):
            eliteUrukHai = EliteUrukHai(increasedStats)
            self._wave3.append(eliteUrukHai)
        #创建萨鲁曼
        sauroman = Sauroman(constants.MONSTER_STATS[Sauroman])
        self._wave3.append(sauroman)

        #生成战利品
        description = "进入欧尔桑克石塔所需的两把巨大的黑色钥匙"
        self._keysOfOrthanc = Item("欧尔桑克的钥匙", description, 1, 104)
        self._palatir = Item("帕蓝提尔", "真知晶石", 6, 112)
        self._loot = [self._keysOfOrthanc, self._palatir]
        
    def enter(self, player):
        """
        Action sequence for visiting Isenguard.

        @param player:  The current player.
        """
        print(self._greetings)
        print("")

        #Player goes through series of battles to take Isenguard
        if not self._battle(player):
            return
        print("")

        #Player given option to summit Orthanc
        choice = self._summitPrompt()
        print("")
        
        #Carry out user-dependent script
        if choice == "yes":
            self._summitOrthanc(player)
        else:
            print("You continue on your journey.")
        
    def _battle(self, player):
        """
        Battle sequence for Isenguard.

        @param player:  The current player.
        """
        #Wave 1
        print ("Immediately as you approach the Ring of Isenguard, you are" 
            " greeted with an a wave of Uruk....")
        input("Press enter to continue. ")
        result = battle(player, constants.BattleEngineContext.STORY, self._wave)
        if not result:
            return False
        print("")
        
        #Wave 2
        print ("As you gaze over bodies of your slain enemies, Sauroman the" 
            " Great Wizard appears.")
        input("Press enter to continue. ")
        print("")
        
        print ("Sauroman: \"You shouldn't have come, foolish one. Were you" 
            " haughty enough to think that you could take the Orthanc?\"")
        input("Press enter to continue. ")
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave2)
        if not result:
            return False
        print("")
        
        #Wave 3
        print("Sauroman: \"You stupid fool....\"")
        input("Press enter to continue. ")
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave3)
        if not result:
            return False
        print("")

        #Victory sequence
        print("Isenguard has a new overseer this day.")
        print("")
        
        self._createPort("south")
        
        #Give player loot
        if self._keysOfOrthanc in self._loot:
            print("You have gained the Keys of the Orthanc!")
            print("")
            if player.addToInventory(self._keysOfOrthanc):
                self._loot.remove(self._keysOfOrthanc)
        
    def _summitPrompt(self):
        """
        Solicits user choice. Player given opportunity to summit the Orthanc 
        (Sauroman's Tower).

        @param player:  The current player.
        """
        choice = None
        acceptable = ["yes", "no"]
        print("Would you like to summit the Tower of Orthanc?")
        while choice not in acceptable:
            choice = input("Choice: 'yes' or 'no.' ")
            
        return choice

    def _summitOrthanc(self, player):
        """
        Action sequence given that user has choicen to summit the Orthanc.

        @param player:  The current player.
        """
        #Summiting the Orthanc
        print("You take a brief residence in the Tower of Orthanc!")
        input("Press enter to continue. ")
        print("")
        
        #Give player loot
        if self._palatir in self._loot:
            print("You found Sauroman's Palatir!")
            if player.addToInventory(self._palatir):
                self._loot.remove(self._palatir)
        print("")

        #Story
        print("Congratulations on your victory!")
        print("")