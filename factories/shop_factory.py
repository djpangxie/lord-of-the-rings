#!/usr/bin/python

import math
import random

from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.item_set import ItemSet
from items.unique_items import lowLevelFindableUniques, shopWeaponDist, shopArmorDist, shopPotionDist
import constants


def getItems(region, numItems, quality):
    """
    为商店生成随机物品。

    @param region:       商店所处的地区
    @param numItems:     在商店里可以买到的物品数量
    @param quality:      可能在商店中买到的物品品质。Ranges from 1-20.
    @return:             一个随机生成的商品的ItemSet对象
    """
    items = ItemSet()

    for item in range(numItems):
        # 生成用于确定物品类型的随机数
        randType = random.random()

        # 随机化物品品质
        q = qualityRandomizer(quality)

        # 生成物品并附加到物品列表
        if randType < constants.ShopFactoryConstants.WEAPON_UPPER_LIMIT:
            item = genWeapon(q, region)
            items.addItem(item)
        elif randType < constants.ShopFactoryConstants.ARMOR_UPPER_LIMIT:
            item = genArmor(q, region)
            items.addItem(item)
        elif randType < constants.ShopFactoryConstants.POTION_UPPER_LIMIT:
            item = genPotion(q, region)
            items.addItem(item)
        else:
            # 在游戏中只有高等级的商店才能生成独特的东西
            if constants.ShopFactoryConstants.UNIQUE_QUALITY_REQ <= q and lowLevelFindableUniques:
                item = random.choice(lowLevelFindableUniques)
                items.addItem(item)
            # 低等级级的级商店则会生成额外的药剂
            else:
                item = genPotion(q, region)
                items.addItem(item)

    return items


def qualityRandomizer(quality):
    """
    使用正态分布随机化物品品质。
    
    @param quality:    商店物品的品质
    
    @return:           随机的品质
    """
    # 使用正态分布标准化物品品质
    quality = random.normalvariate(quality, constants.ShopFactoryConstants.STANDARD_DEVIATION)
    quality = math.floor(quality)

    # 确保结果在界限内
    if quality < constants.ShopFactoryConstants.QUALITY_MINIMUM:
        quality = constants.ShopFactoryConstants.QUALITY_MINIMUM
    if quality > constants.ShopFactoryConstants.QUALITY_MAXIMUM:
        quality = constants.ShopFactoryConstants.QUALITY_MAXIMUM

    return quality


def genWeapon(quality, region):
    """
    生成一件武器。
    
    @param quality:     物品的品质
    @param region:      商店的地区
    
    @return:            生成的武器的Item对象
    """
    regionalDist = shopWeaponDist[region]
    acceptableItems = []

    # 创建品质范围
    for weapon in regionalDist:
        lowerBound = regionalDist[weapon][0]
        higherBound = regionalDist[weapon][1]

        # 查找范围内的物品
        if lowerBound <= quality <= higherBound:
            acceptableItems.append(weapon)

    # 从可接受的物品中选择随机抽取的物品
    item = random.choice(acceptableItems)
    return item


def genArmor(quality, region):
    """
    生成一件盔甲。
    
    @param quality:     物品的品质
    @param region:      商店的地区
    
    @return:            生成的盔甲的Item对象
    """
    regionalDist = shopArmorDist[region]
    acceptableItems = []

    # 创建品质范围
    for armor in regionalDist:
        lowerBound = regionalDist[armor][0]
        higherBound = regionalDist[armor][1]

        # 查找范围内的物品
        if lowerBound <= quality <= higherBound:
            acceptableItems.append(armor)

    # 从可接受的物品中选择随机抽取的物品
    item = random.choice(acceptableItems)
    return item


def genPotion(quality, region):
    """
    生成药水。
    
    @param quality:     物品的品质
    @param region:      商店的地区
    
    @return:            生成的药水的Item对象
    """
    regionalDist = shopPotionDist[region]
    acceptableItems = []

    # 创建品质范围
    for potion in regionalDist:
        lowerBound = regionalDist[potion][0]
        higherBound = regionalDist[potion][1]

        # 查找范围内的物品
        if lowerBound <= quality <= higherBound:
            acceptableItems.append(potion)

    # 从可接受的物品中选择随机抽取的物品
    item = random.choice(acceptableItems)
    return item
