#!/usr/bin/python

import random
from math import floor

import constants


def getMonsters(number, region, bonusDifficulty):
    """
    为战斗引擎生成怪物。

    @param number:           生成的怪物数量
    @param region:           玩家当前所在的地区类型
    @param bonusDifficulty:  该地区的难度加成
    """
    monsters = []
    monsterDistribution = constants.REGIONAL_MONSTER_DISTRIBUTION[region]

    for numSpawn in range(number):
        randomNum = random.random()
        for Monster in monsterDistribution:
            lowerLimit = monsterDistribution[Monster][0]
            upperLimit = monsterDistribution[Monster][1]
            if lowerLimit <= randomNum < upperLimit:
                # 获取怪物基础数据
                stats = constants.MONSTER_STATS[Monster]
                # 修改怪物属性以符合难度加成
                modifiedStats = []
                for stat in stats:
                    modifiedStat = stat * (1 + bonusDifficulty)
                    modifiedStat = floor(modifiedStat)
                    modifiedStats.append(modifiedStat)

                monsterSpawn = Monster(modifiedStats)
                monsters.append(monsterSpawn)
                break

    return monsters
