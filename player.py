#!/usr/bin/python

from math import floor

from items.item import Item
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.charm import Charm
from items.item_set import ItemSet
from util.helpers import sortItems
import constants

class Player(object):
    """
    代表玩家。
    """
    def __init__(self, name, location):
        """
        初始化玩家对象。
        
        @param name:             玩家姓名（例如："弗罗多"）
        @param location:         玩家当前所在地区。初始化时，默认为夏尔
        """
        self._name      = name # 玩家姓名字符串
        self._location  = location # 玩家当前所在地区
        
        #初始化玩家属性
        self._money      = constants.PlayerInitialization.MONEY
        self._experience = constants.PlayerInitialization.EXPERIENCE
        self._level      = constants.PlayerInitialization.LEVEL
        
        self._hp          = constants.PlayerInitialization.MAX_HP
        self._maxHp       = constants.PlayerInitialization.MAX_HP
        self._attack      = constants.PlayerInitialization.ATTACK
        self._weightLimit = constants.PlayerInitialization.WEIGHT_LIMIT
        
        #初始化玩家库存和装备
        self._inventory = ItemSet() # 玩家的库存
        self._equipped  = ItemSet() # 玩家的当前装备

        #初始化玩家装备以及饰品的属性加值
        self._weaponAttack = constants.PlayerInitialization.WEAPON_ATTACK
        self._armorDefense = constants.PlayerInitialization.ARMOR_DEFENSE
        
        self._charmAttack   = constants.PlayerInitialization.CHARM_ATTACK
        self._charmDefense  = constants.PlayerInitialization.CHARM_DEFENSE
        self._charmHp       = constants.PlayerInitialization.CHARM_HP

        #初始化玩家最终的攻击力、防御力和最大生命值
        self._totalAttack    = self._attack + self._weaponAttack + self._charmAttack
        self._totalDefense   = self._armorDefense + self._charmDefense
        self._totalMaxHp     = self._maxHp + self._charmHp
        
    def getName(self):
        """
        返回玩家姓名。

        @return:          玩家姓名
        """
        return self._name

    def attack(self, target):
        """
        Allows player to attack target. 

        @param target:    The target player is to attack.
        """
        target.takeAttack(self._totalAttack)
        
    def getAttack(self):
        """
        返回玩家的基础攻击力。
        
        @return:          玩家的基础攻击力
        """
        return self._attack

    def getTotalAttack(self):
        """
        返回玩家的最终攻击力。

        @return:          玩家的最终攻击力
        """
        return self._totalAttack

    def takeAttack(self, attack):
        """
        Allows player to receive an attack.

        @param attack:     The attack player is to receive.
        """
        self._hp = max(self._hp - max(attack - self._totalDefense, 0), 0)
        
    def getTotalDefense(self):
        """
        返回玩家的最终防御力。
        
        @return:     玩家的最终防御力
        """
        return self._totalDefense
        
    def getCharmAttack(self):
        """
        返回玩家佩戴的饰品的攻击加值。
        
        @return:     玩家佩戴的饰品的攻击加值
        """
        return self._charmAttack
        
    def getCharmDefense(self):
        """
        返回玩家佩戴的饰品的防御加值。
        
        @return:     玩家佩戴的饰品的防御加值
        """
        return self._charmDefense
        
    def getCharmHp(self):
        """
        返回玩家佩戴的饰品的最大生命值加值。
        
        @return:     玩家佩戴的饰品的最大生命值加值
        """
        return self._charmHp
        
    def getWeightLimit(self):
        """
        返回玩家的负重上限。
        
        @return:     玩家的负重上限
        """
        return self._weightLimit
        
    def getExperience(self):
        """
        返回玩家的经验值。
        
        @return:    玩家的经验值
        """
        return self._experience

    def increaseExperience(self, newExperience):
        """
        Allows player to receive additional experience.
        Runs _updateLevel() upon receiving additional
        experience.

        @param newExperience:    The experience player 
                                 is to receive.
        """
        self._experience += newExperience
        self._updateLevel()
        
    def getLevel(self):
        """
        返回玩家的等级。
        
        @return:      玩家等级
        """
        return self._level
        
    def _updateLevel(self):
        """
        Levels up player and updates player stats. This method creates a list 
        of levels for which player experiences qualifies. Player level is the 
        highest level for which player experience qualifies. 
        
        After level-up is determined, player stats are updated.
        """
        #Checks to see if player is max level
        if self._level == constants.MAX_LEVEL:
            return
            
        #Check to see if player has leveled up
        currentLevel = self._level
        potentialLevels = []
        
        #Create list of levels for which player experience qualifies
        for level in constants.LEVEL_EXP_REQUIREMENT:
            if self._experience >= constants.LEVEL_EXP_REQUIREMENT[level]:
                potentialLevels.append(level)
        
        #Player level is the highest of the qualified levels
        potentialNewLevel = max(potentialLevels)
        
        #If player has leveled up
        if currentLevel != potentialNewLevel:
            numberLevelUp = potentialNewLevel - currentLevel
            self._level = potentialNewLevel
            print("\n%s leveled up! %s is now level %s!" \
                  % (self._name, self._name, self._level))
                  
            #Updates player level and stats
            for level in range(numberLevelUp):
                self._maxHp = floor(self._maxHp * constants.HP_STAT)
                self._totalMaxHp = self._maxHp + self._charmHp
                self._attack = floor(self._attack * constants.ATTACK_STAT)
                self._totalAttack = (self._attack + self._weaponAttack + 
                    self._charmAttack)
                self._weightLimit = floor(self._weightLimit * 
                    constants.WEIGHT_LIMIT_STAT)
            
    def getHp(self):
        """
        返回玩家的当前生命值。

        @return:    玩家的当前生命值
        """
        return self._hp

    def getMaxHp(self):
        """
        返回玩家的最大生命值。

        @return:    玩家的最大生命值
        """
        return self._maxHp
        
    def getTotalMaxHp(self):
        """
        返回玩家的最终最大生命值。

        @return:    玩家的最终最大生命值
        """
        return self._totalMaxHp
        
    def heal(self, amount):
        """
        Allows player to heal up to totalMaxHp.

        @param amount:    The amount of hp to be healed.
        """
        #If amount that player may be healed is less than amount possible
        if self._totalMaxHp - self._hp < amount:
            amountHealed = self._totalMaxHp - self._hp
            
        #If amount that player may be healed is greater than or equal to the 
        #amount possible
        else:
            amountHealed = amount
            
        self._hp += amountHealed

    def equip(self, item):
        """
        使角色装备一件物品。

        前提条件：
        -物品在库存中。
        -物品必须是武器、盔甲或者饰品对象。
        -物品对象本身不在装备栏中。

        @param item:    要装备的物品
        """
        #检查是否满足先决条件
        if item not in self._inventory:
            statement =  "%s 当前不在库存中！" % item.getName()
            return statement
        if not (isinstance(item, Armor) or isinstance(item, Weapon) or isinstance(item, Charm)):
            statement = "要装备的物品必须是武器、盔甲或者饰品。"
            return statement
        if item in self._equipped:
            statement =  "%s 已经装备好了。" % item.getName()
            return statement
        
        #卸下当前装备的盔甲或武器
        for currentItem in self._equipped:
            if isinstance(item, Weapon) and isinstance(currentItem, Weapon):  
                self.unequip(currentItem)
            elif isinstance(item, Armor) and isinstance(currentItem, Armor):
                self.unequip(currentItem)

        #装备新的盔甲或武器
        self._equipped.addItem(item)
        if isinstance(item, Weapon):
            self._weaponAttack = item.getAttack()
            self._totalAttack = self._attack + self._weaponAttack + self._charmAttack
        elif isinstance(item, Armor):
            self._armorDefense = item.getDefense()
            self._totalDefense = self._armorDefense + self._charmDefense
        elif isinstance(item, Charm):
            self._charmAttack += item.getAttack()
            self._charmDefense += item.getDefense()
            self._charmHp += item.getHp()
            self._totalAttack = self._attack + self._weaponAttack + self._charmAttack
            self._totalDefense = self._armorDefense + self._charmDefense
            self._totalMaxHp = self._maxHp + self._charmHp

        statement = "%s 装备上了 %s。" %(self._name, item.getName())

        #为装备栏排序
        sortItems(self._equipped)

        return statement
        
    def unequip(self, item):
        """
        使角色卸下当前装备的物品。

        @param item:    要卸下的物品
        """
        #前提 - 该物品已存在当前装备栏中。
        if item not in self._equipped:
            statement = "%s 不在装备栏中。" % item.getName()
            return statement

        #卸下装备并更新玩家数据
        self._equipped.removeItem(item)
        
        if isinstance(item, Weapon):
            self._weaponAttack = 0
            self._totalAttack = self._attack + self._weaponAttack + self._charmAttack
        if isinstance(item, Armor):
            self._armorDefense = 0
            self._totalDefense = self._armorDefense + self._charmDefense
        if isinstance(item, Charm):
            charmAttack = item.getAttack()
            charmDefense = item.getDefense()
            charmHp = item.getHp()
            
            self._charmAttack -= charmAttack
            self._charmDefense -= charmDefense
            self._charmHp -= charmHp
            
            self._totalAttack = self._attack + self._weaponAttack + self._charmAttack
            self._totalDefense = self._armorDefense + self._charmDefense
            self._totalMaxHp = self._maxHp + self._charmHp
            
        statement = "%s 卸下了 %s。" % (self._name, item.getName())
        return statement

    def getEquipped(self):
        """
        返回玩家当前装备的ItemSet对象。

        @return:    玩家当前装备的ItemSet对象
        """
        return self._equipped
    
    def addToInventory(self, item):
        """
        将物品添加到玩家库存中。

        @param item:   要添加到玩家库存的物品
        
        @return:       如果执行成功则返回True，否则返回False
        """
        inventory = self._inventory
        
        #如果该项目不是物品
        if not isinstance(item, Item):
            errorMsg = "不是一个物品对象。"
            raise AssertionError(errorMsg)
        
        #物品不能已在库存中
        if item in inventory:
            print("物品已在库存中。")
        
        #检查库存重量限制
        itemWeight = item.getWeight()
        inventoryWeight = inventory.getWeight()

        if itemWeight + inventoryWeight > self._weightLimit:
            print("你负担过重。")
            return False

        #成功执行
        inventory.addItem(item)
        sortItems(inventory)
        print("已将 %s 添加进库存！" % item.getName())
        return True
            
    def removeFromInventory(self, item):
        """
        Removes an item from inventory. If item is currently 
        equipped, unequips item.

        @param item:   The item to be removed.
        """
        #Item must be in inventory
        if not item in self._inventory:
            return
        
        #Unequip if necessary
        if item in self._equipped:
            self.unequip(item)
            
        self._inventory.removeItem(item)
    
    def getInventory(self):
        """
        返回玩家的库存的ItemSet对象。

        @return:    玩家的库存的ItemSet对象
        """
        return self._inventory
   
    def getMoney(self):
        """
        返回玩家拥有的金钱数。

        @return:    玩家拥有的金钱数
        """
        return self._money

    def increaseMoney(self, amount):
        """
        Increases player money.
        """
        if amount < 0:
            errorMsg = "Method increaseMoney() was given a negative value."
            raise AssertionError(errorMsg)

        self._money += amount
        
    def decreaseMoney(self, amount):
        """
        Decreases player money.
        """
        if amount < 0:
            errorMsg = "Method decreaseMoney() was given a negative value."
            raise AssertionError(errorMsg)

        self._money -= amount
    
    def canMoveNorth(self):
        """
        判断玩家是否可以向北旅行。

        @return:    如果可以则为True，否则为False
        """
        if self._location.getExit(constants.Direction.NORTH):
            return True

        return False

    def canMoveSouth(self):
        """
        判断玩家是否可以向南旅行。

        @return:    如果可以则为True，否则为False
        """
        if self._location.getExit(constants.Direction.SOUTH):
            return True

        return False

    def canMoveEast(self):
        """
        判断玩家是否可以向东旅行。

        @return:    如果可以则为True，否则为False
        """
        if self._location.getExit(constants.Direction.EAST):
            return True

        return False

    def canMoveWest(self):
        """
        判断玩家是否可以向西旅行。

        @return:    如果可以则为True，否则为False
        """
        if self._location.getExit(constants.Direction.WEST):
            return True

        return False

    def moveNorth(self):
        """
        将玩家向北移动到连接的地区。
        """
        northSpace = self._location.getExit(constants.Direction.NORTH) 
        
        #如果北边的地区不存在，什么也不做
        if not northSpace:
            return
            
        #...否则，移动到新的地区
        if not isinstance(northSpace, list):
            self._location = northSpace
        else:
            self._moveList(northSpace)

    def moveSouth(self):
        """
        将玩家向南移动到连接的地区
        """
        southSpace = self._location.getExit(constants.Direction.SOUTH)

        #如果南边的地区不存在，什么也不做
        if not southSpace:
            return
            
        #...否则，移动到新的地区
        if not isinstance(southSpace, list):
            self._location = southSpace
        else:
            self._moveList(southSpace)

    def moveEast(self):
        """
        将玩家向东移动到连接的地区。
        """
        eastSpace = self._location.getExit(constants.Direction.EAST)

        #如果东边的地区不存在，什么也不做
        if not eastSpace:
            return
            
        #...否则，移动到新的地区
        if not isinstance(eastSpace, list):
            self._location = eastSpace
        else:
            self._moveList(eastSpace)

    def moveWest(self):
        """
        将玩家向西移动到连接的地区。
        """
        westSpace = self._location.getExit(constants.Direction.WEST)

        #如果西边的地区不存在，什么也不做
        if not westSpace:
            return
            
        #...否则，移动到新的地区
        if not isinstance(westSpace, list):
            self._location = westSpace
        else:
            self._moveList(westSpace)
    
    def _moveList(self, spaces):
        """
        四个移动命令的辅助方法。处理单个开口通向多个地区的情况。
        """
        acceptableChoices = {}
        choice = None
        
        #征求用户输入
        print("您可以去往以下地区：")
        for space in spaces:
            print("\t-%s" % space.getName())
            acceptableChoices[space] = space.getName()
        print("")
        
        while choice not in list(acceptableChoices.values()):
            choice = input("你想去哪里？（复制地名并输入）：")

        #移动到新的地区
        for pair in list(acceptableChoices.items()):
            if choice in pair:
                space = pair[0]
                break
        self._location = space
        
    def getLocation(self):
        """
        返回玩家当前所在地区。

        @return:    玩家当前所在地区
        """
        return self._location