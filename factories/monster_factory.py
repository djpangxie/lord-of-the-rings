#!/usr/bin/python

from monsters.monster import Monster
import constants

from math import floor
import random

def getMonsters(number, region, bonusDifficulty):
    """
    Generates enemies for the battle sequence.

    @param number:      The number of monsters to generate.
    @param region:      The region of the map Player is currently in.
    @param difficulty:  The number of enemies to generate.
    """
    monsters = []
        
    #Spawn monsters
    for monster in range(number):
        #For region Eriador
        if region == constants.RegionType.ERIADOR:
            #Determine which monster is to be spawned
            randomNum = random.random()
            for Monster in constants.RegionMonsterDistribution.ERIADOR:
                if randomNum < constants.RegionMonsterDistribution.ERIADOR[Monster]:
                    #Find monster stats
                    stats = constants.MONSTER_STATS[Monster]
                    #Modify monster stats for bonusDifficulty
                    modifiedStats = []
                    for stat in stats:
                        modifiedStat = (1 + bonusDifficulty) * stat
                        modifiedStat = floor(modifiedStat)
                        modifiedStats.append(modifiedStat)
                    #Instantiate and append monster to monsters
                    monster = Monster(modifiedStats)
                    monsters.append(monster)
                    #There should only be one monster spawned per iteration
                    break

        elif region == constants.RegionType.BARROW_DOWNS:
            pass
        
        elif region == constants.RegionType.HIGH_PASS:
            #Determine which monster is to be spawned
            randomNum = random.random()
            for Monster in constants.RegionMonsterDistribution.HIGH_PASS:
                if randomNum < constants.RegionMonsterDistribution.HIGH_PASS[Monster]:
                    #Find monster stats
                    stats = constants.MONSTER_STATS[Monster]
                    #Modify monster stats for bonusDifficulty
                    modifiedStats = []
                    for stat in stats:
                        modifiedStat = (1 + bonusDifficulty) * stat
                        modifiedStat = floor(modifiedStat)
                        modifiedStats.append(modifiedStat)
                    #Instantiate and append monster to monsters
                    monster = Monster(modifiedStats)
                    monsters.append(monster)
                    #There should only be one monster spawned per iteration
                    break
                
        elif region == constants.RegionType.ENEDWAITH:
            pass
        elif region == constants.RegionType.EREGION:
            pass
        elif region == constants.RegionType.RHOVANION:
            pass
        elif region == constants.RegionType.ROHAN:
            pass
        elif region == constants.RegionType.GONDOR:
            pass
        elif region == constants.RegionType.MORDOR:
            pass
        else:
            errorMsg = "Unsupported region type for monster spawn."
            raise AssertionError(errorMsg)

    return monsters
