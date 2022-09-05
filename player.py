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
        @param location:         玩家初始所在地区，默认为夏尔
        """
        self._name = name  # 玩家姓名字符串
        self._location = location  # 玩家当前所在地区

        # 初始化玩家属性
        self._money = constants.PlayerInitialization.MONEY
        self._experience = constants.PlayerInitialization.EXPERIENCE
        self._level = constants.PlayerInitialization.LEVEL

        self._hp = constants.PlayerInitialization.MAX_HP
        self._maxHp = constants.PlayerInitialization.MAX_HP
        self._attack = constants.PlayerInitialization.ATTACK
        self._weightLimit = constants.PlayerInitialization.WEIGHT_LIMIT

        # 初始化玩家库存和装备
        self._inventory = ItemSet()  # 玩家的库存
        self._equipped = ItemSet()  # 玩家的当前装备

        # 初始化玩家装备以及饰品的属性加值
        self._weaponAttack = constants.PlayerInitialization.WEAPON_ATTACK
        self._armorDefense = constants.PlayerInitialization.ARMOR_DEFENSE

        self._charmAttack = constants.PlayerInitialization.CHARM_ATTACK
        self._charmDefense = constants.PlayerInitialization.CHARM_DEFENSE
        self._charmHp = constants.PlayerInitialization.CHARM_HP

        # 初始化玩家最终的攻击力、防御力和最大生命值
        self._totalAttack = self._attack + self._weaponAttack + self._charmAttack
        self._totalDefense = self._armorDefense + self._charmDefense
        self._totalMaxHp = self._maxHp + self._charmHp

    def getName(self):
        """
        返回玩家姓名。

        @return:          玩家姓名
        """
        return self._name

    def attack(self, target):
        """
        使玩家攻击怪物。

        @param target:    怪物对象
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
        玩家受到攻击。

        @param attack:     怪物的攻击力

        @return:           受到的伤害量
        """
        damage = max(attack - self._totalDefense, 0)
        self._hp = max(self._hp - damage, 0)
        return damage

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
        使玩家获得的经验，并执行_updateLevel()以进行可能的升级。

        @param newExperience:    玩家获得的经验
        """
        self._experience += newExperience
        self._updateLevel()

    def reduceExperience(self):
        """
        使玩家减少经验，这会在输掉一场战斗后执行。
        """
        self._experience = floor(self._experience * constants.LOSE_REDUCE_EXP)

    def getLevel(self):
        """
        返回玩家的等级。
        
        @return:      玩家等级
        """
        return self._level

    def _updateLevel(self):
        """
        提升玩家等级并更新玩家数据。该方法创建了一个玩家经验符合条件的等级列表。
        玩家等级是玩家经验符合的最高等级。确定升级后，更新玩家统计数据。
        """
        # 检查玩家是否达到最高等级
        if self._level == constants.MAX_LEVEL:
            return

        # 检查玩家是否升级
        currentLevel = self._level
        potentialLevels = []

        # 创建玩家经验符合条件的等级列表
        for level in constants.LEVEL_EXP_REQUIREMENT:
            if self._experience >= constants.LEVEL_EXP_REQUIREMENT[level]:
                potentialLevels.append(level)

        potentialNewLevel = max(potentialLevels)

        # 如果玩家的等级提高了
        if currentLevel < potentialNewLevel:
            numberLevelUp = potentialNewLevel - currentLevel
            self._level = potentialNewLevel
            print("\n%s 升到了 %s 级！" % (self._name, self._level))

            # 更新玩家等级和数据
            for level in range(numberLevelUp):
                self._maxHp = floor(self._maxHp * constants.HP_STAT)
                self._totalMaxHp = self._maxHp + self._charmHp
                self._attack = floor(self._attack * constants.ATTACK_STAT)
                self._totalAttack = self._attack + self._weaponAttack + self._charmAttack
                self._weightLimit = floor(self._weightLimit * constants.WEIGHT_LIMIT_STAT)

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
        恢复玩家的生命值。

        @param amount:    治疗量
        """
        if self._totalMaxHp - self._hp < amount:
            amountHealed = self._totalMaxHp - self._hp
        else:
            amountHealed = amount

        self._hp += amountHealed

        if self._hp <= 0:
            self._hp = 1

    def equip(self, item):
        """
        使角色装备一件物品。

        前提条件：
        -物品在库存中。
        -物品必须是武器、盔甲或者饰品对象。
        -物品对象本身不在装备栏中。

        @param item:    要装备的物品
        """
        # 检查是否满足先决条件
        if item not in self._inventory:
            statement = "%s 当前不在库存中！" % item.getName()
            return statement
        if not (isinstance(item, Armor) or isinstance(item, Weapon) or isinstance(item, Charm)):
            statement = "要装备的物品必须是武器、盔甲或者饰品。"
            return statement
        if item in self._equipped:
            statement = "%s 早就被装备上了。" % item.getName()
            return statement

        # 卸下当前装备的盔甲或武器
        for currentItem in self._equipped:
            if isinstance(item, Weapon) and isinstance(currentItem, Weapon):
                self.unequip(currentItem)
            elif isinstance(item, Armor) and isinstance(currentItem, Armor):
                self.unequip(currentItem)

        # 装备新的盔甲或武器
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

        statement = "%s 装备上了 %s" % (self._name, item.getName())

        # 为装备栏排序
        sortItems(self._equipped)

        return statement

    def unequip(self, item):
        """
        使角色卸下当前装备的物品。

        @param item:    要卸下的物品
        """
        # 前提 - 该物品已存在当前装备栏中。
        if item not in self._equipped:
            statement = "%s 不在装备栏中。" % item.getName()
            return statement

        # 卸下装备并更新玩家数据
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

        statement = "%s 卸下了 %s" % (self._name, item.getName())
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

        # 如果该项目不是物品
        if not isinstance(item, Item):
            errorMsg = "不是一个物品对象。"
            raise AssertionError(errorMsg)

        # 检查库存重量限制
        itemWeight = item.getWeight()
        inventoryWeight = inventory.getWeight()

        if itemWeight + inventoryWeight > self._weightLimit:
            print("你负担过重。")
            return False

        # 成功执行
        inventory.addItem(item)
        sortItems(inventory)
        print("已将 %s 添加进库存！" % item.getName())
        return True

    def removeFromInventory(self, item):
        """
        从库存中移除一件物品。如果该物品当前已被装备上，则会先卸下该装备。

        @param item:   要移除的物品
        """
        # 物品必须在库存中
        if not item in self._inventory:
            return

        # 必要时卸下装备
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
        增加玩家金钱。
        """
        if amount < 0:
            errorMsg = "increaseMoney()是增加金钱的方法，不能减少金钱。"
            raise AssertionError(errorMsg)

        self._money += amount

    def decreaseMoney(self, amount):
        """
        减少玩家金钱。
        """
        if amount < 0:
            errorMsg = "reductionMoney()是减少金钱的方法，不能增加金钱。"
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

        # 如果北边的地区不存在，什么也不做
        if not northSpace:
            return

        # ...否则，移动到新的地区
        if not isinstance(northSpace, list):
            self._location = northSpace
        else:
            self._moveList(northSpace)

    def moveSouth(self):
        """
        将玩家向南移动到连接的地区
        """
        southSpace = self._location.getExit(constants.Direction.SOUTH)

        # 如果南边的地区不存在，什么也不做
        if not southSpace:
            return

        # ...否则，移动到新的地区
        if not isinstance(southSpace, list):
            self._location = southSpace
        else:
            self._moveList(southSpace)

    def moveEast(self):
        """
        将玩家向东移动到连接的地区。
        """
        eastSpace = self._location.getExit(constants.Direction.EAST)

        # 如果东边的地区不存在，什么也不做
        if not eastSpace:
            return

        # ...否则，移动到新的地区
        if not isinstance(eastSpace, list):
            self._location = eastSpace
        else:
            self._moveList(eastSpace)

    def moveWest(self):
        """
        将玩家向西移动到连接的地区。
        """
        westSpace = self._location.getExit(constants.Direction.WEST)

        # 如果西边的地区不存在，什么也不做
        if not westSpace:
            return

        # ...否则，移动到新的地区
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

        # 征求用户输入
        print("您可以去往以下地区：")
        for space in spaces:
            print("\t-%s" % space.getName())
            acceptableChoices[space] = space.getName()
        print("")

        while choice not in list(acceptableChoices.values()):
            choice = input("你想去哪里？（复制地名并输入）：")

        # 移动到新的地区
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
