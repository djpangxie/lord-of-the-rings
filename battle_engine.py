#!/usr/bin/python

import math
import random

import factories.monster_factory
from commands.use_potion_command import UsePotionCommand
from util.helpers import triangular
from items.unique_items import lowLevelFindableUniques
from items.unique_items import highLevelFindableUniques
from items.unique_items import eliteLevelFindableUniques
import constants

def battle(player, context, monsters = None):
    """
    指环王的战斗引擎。

    @param player:     玩家对象
    @param context:    战斗引擎的模式，战斗引擎在不同模式下有不同的表现
                       战斗要么是随机战斗，要么是基于故事的战斗（例如：BOSS战）
    @param monsters:   用于基于故事的战斗的可选参数，包含要战斗的怪物列表
                       
    @return:           如果战斗获胜则为True；否则为False

    随机战斗和剧情战斗的区别：
    -随机战斗：怪物工厂由战斗引擎调用，怪物由怪物工厂提供。玩家可以在随机战斗中成功奔跑。
    -剧情战斗：怪物必须通过monsters参数提供。玩家不能从剧情战斗中逃跑。
    """
    #战斗设置
    output = _battleSetup(player, context)
    if context == constants.BattleEngineContext.RANDOM:
        bonusDifficulty = output[0]
        monsters = output[1]
        #If no monsters are spawned
        if len(monsters) == 0:
            return
    else:
        bonusDifficulty = output
        
    earnings = [0, 0]
    
    #Main battle sequence
    while len(monsters) != 0:
        #Display enemy monsters
        print("Monsters:")
        for monster in monsters:
            print("\t%s: %s" % (monster.getName(), monster.getDescription()))
        print("")
        
        #Solicit user input
        choice = None
        acceptable = ["attack", "use potion", "run", "explode"]
        while choice not in acceptable:
            choice = input("You may: 'attack', 'use potion', 'run.' ")
        
        #Player attack option
        if choice == 'attack':
            earnings = _playerAttackPhase(player, monsters, bonusDifficulty, earnings)
            
        #Use potion option
        elif choice == "use potion":
            _usePotion(player)
            
        #Run option
        elif choice == "run":
            if context == constants.BattleEngineContext.RANDOM:
                if random.random() < constants.BattleEngine.RUN_PROBABILITY_SUCCESS:
                    print("You ran away succesfully!")
                    print("")
                    return True
                else:
                    print("Your path is blocked!")
            else:
                print("Your path is blocked!")
                
        #Code - eliminates all enemies
        elif choice == "explode":
            monsters = []
            earnings = [0, 0]

        #Break between player and monster phases
        input("Press enter to continue. ")
        print("")

        #Monsters attack phase
        continueBattle = _monsterAttackPhase(player, monsters)
        
        #Escape sequence given battle loss
        if not continueBattle:
            print("")
            print("Gandalf bails you out.")
            player.heal(1)
            
            return False
        
    #Battle end sequence - loot received
    _endSequence(player, earnings)
    
    return True

def _battleSetup(player, context):
    """
    Generates variables for battle engine and prints battle
    splash screen.
    """
    #For random battles
    if context == constants.BattleEngineContext.RANDOM:
        #Create variables
        location = player.getLocation()
        region = location.getRegion()
        bonusDifficulty = location.getBattleBonusDifficulty()

        #Spawn monsters
        monsterCount = _monsterNumGen(player)
        monsters = factories.monster_factory.getMonsters(monsterCount, region, 
        bonusDifficulty)

        #Declare battle
        print("Zonkle-tronks! Wild monsters appeared!")
        print("")

        return bonusDifficulty, monsters
    
    #For story-based battles
    elif context == constants.BattleEngineContext.STORY:
        #Create variables
        location = player.getLocation()
        region = location.getRegion()
        bonusDifficulty = location.getBattleBonusDifficulty()
    
        #Display splash screen
        print("""
()==[:::::::::::::> ()==[:::::::::::::> ()==[:::::::::::::>
""")
        return bonusDifficulty
    
    else:
        errorMsg = "_battleSetup given invalid context parameter."
        raise AssertionError(errorMsg)

def _monsterNumGen(player):
    """
    Helper function used to determine the number of monsters to spawn.
    
    Default spawn comes from a parameter supplied by space. A normal 
    distribution is applied to introduce variation.
    
    @param player:     Player object.

    @return:           Number of monsters to spawn.
    """
    location = player.getLocation()
    region = location.getRegion()
    bonusDifficulty = location.getBattleBonusDifficulty()

    #Calculate region spawn
    if region == constants.RegionType.ERIADOR:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.ERIADOR
    elif region == constants.RegionType.BARROW_DOWNS:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.BARROW_DOWNS
    elif region == constants.RegionType.HIGH_PASS:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.HIGH_PASS
    elif region == constants.RegionType.ENEDWAITH:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.ENEDWAITH
    elif region == constants.RegionType.MORIA:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.MORIA
    elif region == constants.RegionType.RHOVANION:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.RHOVANION   
    elif region == constants.RegionType.ROHAN:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.ROHAN       
    elif region == constants.RegionType.GONDOR:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.GONDOR      
    elif region == constants.RegionType.MORDOR:
        monsterCount = (1 + bonusDifficulty) * constants.RegionBaseSpawn.MORDOR
    else:
        errorMsg = "Invalid region - region base monster determination."
        raise AssertionError(errorMsg)
        
    #Apply normal distribution to introduce variation
    standardDeviation = monsterCount/constants.BattleEngine.STANDARD_DEVIATION
    
    monsterCount = random.normalvariate(monsterCount, standardDeviation)
    monsterCount = max(math.floor(monsterCount), 1)
    monsterCount = int(monsterCount)
    
    return monsterCount

def _playerAttackPhase(player, monsters, bonusDifficulty, earnings):
    """
    When the user gets to attack a single monster object.
    If monster health is reduced to zero, monster is removed
    from battle.

    Additionally, experience and money is calculated for winnings.

    @param player:        The player object.
    @param monsters:      The list of monster objects.
    @param earnings:      2-element tuple caring battle earnings. First element
                          is money earned and second is experience received. 
                          Earnings needs to be passed in between successive 
                          function calls to update battle earnings.
    
    @return:              2-element tuple carrying battle earnings.
                          First element is money earned, second
                          element is experience received.
    """
    #Starting battle earnings
    money      = earnings[0]
    experience = earnings[1]

    #Solicit attack target
    target = input("Whom? ")
    print("")
    #Find monster object
    for monster in monsters:
        if monster.getName() == target:
            #Carry out attack
            player.attack(monster)
            print(("%s did %s damage to %s!" % (player.getName(), 
            player.getTotalAttack(), monster.getName())))
            #If monster is still alive
            if monster.getHp() > 0:
                print(("%s has %s hp remaining." % (monster.getName(), 
                monster.getHp())))
            #If monster has died
            else:
                print("%s" % monster.getDeathString())
                #Generate earnings from winning battle
                expIncrease = monster.getExperience() * (1 + bonusDifficulty)
                experience += expIncrease
                money += math.floor(expIncrease/constants.BattleEngine.MONEY_CONSTANT)
                #Remove monster from monsters list
                for monster in monsters:
                    if monster.getName() == target:
                        monsters.remove(monster)
                        #No need to keep iterating through monsters
                        break
            #No need to keep iterating through monsters
            break
    else:
        print("%s looks at you in confusion." % player.getName())
        
    return money, experience

def _usePotion(player):
    """
    Creates an additional UsePotionCommand object
    for battle purposes only and then executes the 
    action sequence of this usePotion.

    @param player:   The player object.
    """
    usePotionCmd = UsePotionCommand(" ", " ", player)
    usePotionCmd.execute()

def _monsterAttackPhase(player, monsters):
    """
    Monster attack phase - when monsters attack player.

    @param player:      The player object.
    @param monsters:    The offending list of monsters.

    @return:            True if battle is to continue. False
                        otherwise.
    """
    #Monsters attack
    for monster in monsters:
        monster.attack(player)
        print(("%s %s for %s damage!" % (monster.getName(), 
        monster.getAttackString(), monster.getAttack())))
        print("%s has %s HP remaining." % (player.getName(), player.getHp()))
        
        #Battle ends
        if player.getHp() == 0:
            print("")
            return False
    
    if monsters:
        input("Press enter to continue. ")
        print("")
    
    #Battle continuation
    return True

def _itemFind(player, experience):
    """
    Calculates whether player finds an item and which item he finds.
    
    @param player:         The player object.
    @param experience:     The experience gained from the battle.
    """
    location = player.getLocation()
    
    #Item find for low-level uniques
    lowLevel = triangular(constants.ItemFind.lowLevel)
    if experience > lowLevel and lowLevelFindableUniques:
        item = random.choice(lowLevelFindableUniques)
        print("You found %s!" % item.getName())
        if not player.addToInventory(item):
            location.addItem(item)

    #Item find for high-level uniques
    highLevel = triangular(constants.ItemFind.highLevel)
    if experience > highLevel and highLevelFindableUniques:
        item = random.choice(highLevelFindableUniques)
        print("You found %s!" % item.getName())
        if not player.addToInventory(item):
            location.addItem(item)
            
    #Item find for elite-level uniques
    eliteLevel = triangular(constants.ItemFind.eliteLevel)
    if experience > eliteLevel and eliteLevelFindableUniques:
        item = random.choice(eliteLevelFindableUniques)
        print("You found %s!" % item.getName())
        if not player.addToInventory(item):
            location.addItem(item)
    
def _endSequence(player, earnings):
    """
    Battle cleanup:
    -Victory sequence displayed.
    -Player experience and money increase.

    @param player:      The player object.
    @param earnings:    2-element tuple: first element is 
                        money and second is experience.
    """
    money = earnings[0]
    experience = earnings[1]
    
    #Calculate splash screen variables
    victoryDeclaration = "Enemies are vanguished!"
    gainsDeclaration = ("%s gains %s %s and %s experience!" 
    % (player.getName(), money, constants.CURRENCY, experience))
    
    lengthBar = len(gainsDeclaration)
    victoryDeclaration = victoryDeclaration.center(lengthBar)
    bar = "$" * lengthBar
    
    #Victory sequence
    print(bar)
    print(victoryDeclaration)
    print(gainsDeclaration)
    _itemFind(player, experience)
    player.increaseMoney(money)
    player.increaseExperience(experience)
    print(bar)
    print("")