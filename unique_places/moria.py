#!/usr/bin/python

from unique_place import UniquePlace
from battle_engine import battle
from items.item import Item
from items.weapon import Weapon
from items.armor import Armor
import constants

import random

class Moria(UniquePlace):
    """
    墨瑞亚是迷雾山脉南部中的独特地点。在托尔金的宇宙中，墨瑞亚是一个巨大的地下城市，由矮人建造，现在已被奥克占领。
    
    如果玩家访问墨瑞亚，他在墨瑞亚花费的时间将是一个随机生成的值，在15-25回合之间。
    在每个回合中，玩家都有机会遇到一群奥克。每一次遭遇都会增加未来遭遇的概率，直到玩家不断地从奥克手中逃跑。

    这是如何工作的：
    -有三种“旅行”方式：低风险旅行、中风险旅行和高风险旅行。调用哪个方法取决于self._danger。
    -如果玩家遇到怪物，self._danger加一。
    -三种旅行方式中的每一种都有自己的PDF，用于确定玩家是否遇到怪物。
    
    补充说明：
    -玩家有机会在墨瑞亚遇到炎魔。炎魔是一个非常强大的怪物，玩家应该逃离它。
    -玩家在穿越墨瑞亚时有机会拾取物品。
    """
    def __init__(self, name, description, greetings):
        """
        初始化墨瑞亚。
        
        @param name:            独特地点名称
        @param description:     独特地点的描述
        @param greetings:       玩家进入该独特地点时得到的问候
        """
        UniquePlace.__init__(self, name, description, greetings)
        
        #初始化危险跟踪器
        self._danger = 0
        
        #低风险活动的字符串
        self._sneakString = ["你继续穿过狭窄的大厅，试图避免被发现......",
        "你匍匐过一个腐烂的图书馆......",
        "你匍匐在矿井中....",
        "你偷偷穿过一些古老的隧道......",
        "你爬过迷宫般的机械群......",
        "你偷偷溜过一连串的尸体......",
        "你偷偷溜过一些奇怪的石碑......"]
        
        #中风险活动的字符串
        self._neutralString = ["你发现楼梯上堆满了矮人战士的尸体。",
        "你经过一个巨大的矿井。",
        "你似乎迷路了，然后转身回去。",
        "你发现自己在一个巨大的大厅里，尽头是一个蜿蜒的楼梯。",
        "你路过曾经是聚会场所的地方。",
        "你藉由相信自己的直觉，转了一系列的弯。",
        "你发现自己被困住了，必须转身回去。"]
        
        #遭遇战斗的字符串
        self._encounterString = ["你听到一些脚步声......",
        "你觉得自己看到一些影子在移动......",
        "你听到一连串激动的咕哝声....",
        "你看到影子在远处飞快地移动....",
        "你听到黑暗中的低语...."]
        
        #如果玩家正在躲避怪物，则为字符串
        self._runString = ["你从一些腐烂的尸体上跑过！",
        "你跑过一个螺旋楼梯！",
        "你沿着一些矿车飞奔！",
        "你沿着圆柱大厅冲刺！",
        "你沿着一个大矿井冲刺！",
        "你飞快地跑过一些古墓！",
        "你爬过了一堆瓦砾！"]
        
        #生成战利品
        description = "取自一个被杀的矮人战士"
        weapon = Weapon("生锈的斧头", description, 6, 8, 12)
        description = "矮人工匠用过的锤子"
        weapon2 = Weapon("矮人锤", description, 10, 12, 16)
        description = "沉浸在历史中"
        weapon3 = Weapon("艾文", description, 8, 22, 18)
        description = "具有历史意义"
        weapon4 = Weapon("杜恩海姆", description, 4, 18, 3)
        description = "老旧但仍然有效"
        armor = Armor("铁帽", description, 3, 4, 1)
        description = "可能会增加魔力知觉"
        armor2 = Armor("旅行之靴", description, 2, 8, 2)
        description = "中洲最稀有的金属之一"
        item = Item("秘银", description, 0, 84)
        description = "神奇的性质？"
        item2 = Item("古代符文", description, 2, 42)
        self._loot = [weapon, weapon2, weapon3, weapon4, armor, armor2, item, item2]
        
    def enter(self, player):
        """
        Action sequence for Moria.
        
        @param player:   The current player.
        """
        #Story
        print(self._greetings)
        print("")
        
        print ("You enter into a once-glorious hall, moving quickly among" 
            " the shadows.")
        input("Press enter to continue. ")
        print("")
        
        #Generate length of time spent in Moria
        timeInMoria = random.randrange(15, 25)

        #Player journeys through Moria
        for time in range(timeInMoria):
            if self._danger < constants.MORIA_LOW_RISK_UPPER_LIMIT:
                result = self._lowRiskTravel(player)
            elif self._danger < constants.MORIA_MED_RISK_UPPER_LIMIT:
                result = self._mediumRiskTravel(player)
            else:
                result = self._highRiskTravel(player)
            
            #Unpack results
            statement = result[0]
            battleOccurence = result[1]
                        
            #Execute action sequence
            print(statement)
            input("Press enter to continue. ")
            print("")
            
            if battleOccurence:
                result = battle(player, constants.BattleEngineContext.RANDOM)
                if not result:
                    return
        
        #Ending sequence
        print("You emerge from the Mines!")
        input("Press enter to continue. ")
        print("")
        
        self._createPort("east")
        
    def _lowRiskTravel(self, player):
        """
        Determines outcome of the player as he ventures through the 
        Mines of Moria.
        
        @param player:  The current player.
        """
        chance = random.random()
        if chance < constants.MORIA_LOW_RISK_SNEAK_UPPER_LIMIT:
            statement = random.choice(self._sneakString)
            battle = False
            self._itemFind(player)
        elif chance < constants.MORIA_LOW_RISK_NEUTRAL_UPPER_LIMIT:
            statement = random.choice(self._neutralString)
            battle = False
            self._itemFind(player)
        else:
            statement = random.choice(self._encounterString)
            self._danger += 1
            battle = True
        
        return statement, battle
            
    def _mediumRiskTravel(self, player):
        """
        Determines outcome of the player as he ventures through the 
        Mines of Moria.
        
        @param player:  The current player.
        """
        chance = random.random()
        if chance < constants.MORIA_MED_RISK_SNEAK_UPPER_LIMIT:
            statement = random.choice(self._sneakString)
            battle = False
            self._itemFind(player)
        elif chance < constants.MORIA_MED_RISK_NEUTRAL_UPPER_LIMIT:
            statement = random.choice(self._neutralString)
            battle = False
            self._itemFind(player)
        else:
            statement = random.choice(self._encounterString)
            self._danger += 1
            battle = True
               
        return statement, battle
        
    def _highRiskTravel(self, player):
        """
        Determines outcome of the player as he ventures through the 
        Mines of Moria.
        
        @param player:  The current player.
        """
        chance = random.random()
        if chance < constants.MORIA_HIGH_RISK_NEUTRAL_UPPER_LIMIT:
            statement = random.choice(self._neutralString)
            battle = False
            self._itemFind(player)
        else:
            statement = random.choice(self._runString)
            self._danger += 1
            battle = True
        
        return statement, battle
        
    def _itemFind(self, player):
        """
        Helper method that determines if the player finds an item and what 
        item.
        
        @param player:  The current player.
        """
        chance = random.random()
        if self._loot and chance < constants.MORIA_ITEM_FIND_PROB:
            item = random.choice(self._loot)
            print(("You found %s while venturing through the Mines of Moria!" 
                % item.getName()))
            
            if player.addToInventory(item):
                self._loot.remove(item)
            
            input("Press enter to continue. ")
            print("")