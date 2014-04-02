#!/usr/bin/python

from items.item import Item
from items.item_set import ItemSet
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from math import floor

import constants

class Player(object):
    """
    Represents the (human) player.
    """
    def __init__(self, name, location):
        """
        Initializes the player.
        
        @param name:             The name of the player (e.g. "Frodo").
        @param location:         The location of player.
        """
        self._name      = name
        self._location  = location
        self._money     = constants.STARTING_MONEY

        #Initialize player inventory and equipment
        self._inventory = ItemSet()
        self._equipped = ItemSet()

        #Initialize player stats
        self._experience = constants.STARTING_EXPERIENCE
        self._level = constants.STARTING_LEVEL
        
        self._hp = self._level * constants.HP_STAT
        self._maxHp = self._level * constants.HP_STAT
        self._attack = self._level * constants.ATTACK_STAT

        #Initialize items bonuses
        self._weaponAttack = 0
        self._armorDefense = 0

    def getName(self):
        """
        Returns player name.

        @return:          The name of the player.
        """
        return self._name

    def attack(self, target):
        """
        Allows player to attack target. 

        @param target:    The target player is to attack.
        """
        self._totalAttack = self._attack + self._weaponAttack
        target.takeAttack(self._totalAttack)
        
    def getAttack(self):
        """
        Gets a player's total attack power (including items).
        
        @return:          Sum of player attack and weapon attack.
        """
        return self._attack + self._weaponAttack

    def takeAttack(self, attack):
        """
        Allows player to receive an attack.

        @param attack:     The attack player is to receive.
        """
        self._hp = max(self._hp - max(attack - self._armorDefense, 0), 0)
        
    def getExperience(self):
        """
        Return's player experience.
        
        @return:    Returns player experience.
        """
        return self._experience

    def increaseExperience(self, newExperience):
        """
        Allows player to receive additional experience.

        @param newExperience:    The experience player is to receive.
        """
        self._experience += newExperience
        
    def getLevel(self):
        """
        Return's player level.
        
        @return:     Return's player level.
        """
        return self._level
        
    def _updateLevel(self):
        """
        Levels up player and updates player stats. 
        """
        #Checks to see if player has leveled up
        if self._level == constants.MAX_LEVEL:
            return
        if self._level != floor(self._experience/20) + 1:
            self._level = floor(self._experience/20) + 1

            #Player has leveled up. Updates player level and stats.
            print "%s leveled up! %s is now level %s" \
                  %(self._name, self._name, self._level)
            self._maxHp = self._level * constants.HP_STAT
            self._attack = self._level * constants.ATTACK_STAT
                  
    def getHp(self):
        """
        Returns player hp.

        @return:    Player hp.
        """
        return self._hp

    def getMaxHp(self):
        """
        Returns player maximum hp.

        @return:    Player maximum hp.
        """
        return self._maxHp
        
    def heal(self, amount):
        """
        Allows player to heal up to maximum starting hp.

        @param amount:    The amount of hp to be healed.
        """
        maxHp = self._level * constants.HP_STAT

        if maxHp - self._hp < amount:
            amountHealed = maxHp - self._hp
        else:
            amountHealed = amount
            
        self._hp += amountHealed

        print "%s got healed by %s! %s's health is now at %s" %(self._name, amountHealed, self._name, self._hp)
        
    def getAttack(self):
        """
        Returns player attack.
        
        @return:    Player attack.
        """
        return self._attack

    def equip(self, item):
        """
        Allows a character to equip an item in inventory.

        @param item:    The item to be equipped.
        """
        #Check to see if item may be equipped
        if not (item in self._inventory) \
            or not (isinstance(item, Armor) or isinstance(item, Weapon)) \
            or item in self._equipped:
            print ""
            print "Cannot equip %s." %item.getName()

        #Update player to reflect equipment
        else:
            if isinstance(item, Armor):
                self._armor = item
                self._armorDefense = self._armor.getDefense()
            elif isinstance(item, Weapon):
                self._weapon = item
                self._weaponAttack = self._weapon.getAttack()

            #Unequip currently equipped armor/weapon if necessary
            for currentItem in self._equipped:
                if isinstance(currentItem, Weapon) and isinstance(item, Weapon):  
                    self.unequip(currentItem)
                elif isinstance(currentItem, Armor) and isinstance(item, Armor):
                    self.unequip(currentItem)
                
            self._equipped.addItem(item)
            
            print "%s equipped %s." %(self._name, item.getName())
            
    def unequip(self, item):
        """
        Allows a character to unequip a currently equipped item.

        @param item:    The item to be unequipped.
        """
        print ""
        if item in self._equipped:
            self._equipped.removeItem(item)
            
            #Update player to reflect equipment
            if isinstance(item, Armor):
                self._armor = None
                self._armorDefense = 0
            if isinstance(item, Weapon):
                self._weapon = None
                self._weaponAttack = 0
                
            print "%s unequipped %s." %(self._name, item.getName())
            
        else:
            print "Cannot unequip %s." %item.getName()

    def getArmor(self):
        """
        Returns player armor.

        @return:    Player's current armor.
        """
        return self._armor

    def getWeapon(self):
        """
        Returns play weapon.

        @return:    Player's current weapon.
        """
        return self._weapon

    def getEquipped(self):
        """
        Returns the player's currently equipped equipment.

        @return:    Player's current gear.
        """
        return self._equipped
    
    def addInventory(self, item):
        """
        Adds an item to inventory.

        @param item:   The item to be added to inventory.
        """
        if (isinstance(item, Item) or isinstance(item, Potion) or isinstance(item, Weapon) or isinstance(item, Armor)) and (item not in self._inventory):
            print "Added %s to inventory." %item.getName()
            self._inventory.addItem(item)
        else:
            print "Cannot add %s to inventory." %(item)

    def removeInventory(self, item):
        """
        Removes an item from inventory. If item is currently equipped, unequips item.

        @param item:   The item to be removed.
        """
        if item in self._inventory:
            if item in self._equipped:
                self.unequip(item)
            self._inventory.removeItem(item)
    
    def getInventory(self):
        """
        Returns the player's inventory.

        @return:    Player's inventory.
        """
        return self._inventory

    def getMoney(self):
        """
        Returns player's money.

        @return:    Player's money.
        """
        return self._money

    def increaseMoney(self, amount):
        """
        Increases player money.
        """
        if amount <= 0:
            errorMsg = "Method increaseMoney() was given a negative value"
            raise AssertionError(errorMsg)

        self._money += amount
        
    def decreaseMoney(self, amount):
        """
        Decreases player money.
        """
        if amount <= 0:
            errorMsg = "Method decreaseMoney() was given a negative value"
            raise AssertionError(errorMsg)

        self._money -= amount
    
    def canMoveNorth(self):
        """
        Determines if player can move north.

        @return:    True if possible, false otherwise.
        """
        exit = self._location.getExit(constants.Direction.NORTH)

        if exit:
            return True
        return False

    def canMoveSouth(self):
        """
        Determines if player can move south.

        @return:    True if possible, false otherwise.
        """
        exit = self._location.getExit(constants.Direction.SOUTH)

        if exit:
            return True
        return False

    def canMoveEast(self):
        """
        Determines if player can move east.

        @return:    True if possible, false otherwise.
        """
        exit = self._location.getExit(constants.Direction.EAST)

        if exit:
            return True
        return False

    def canMoveWest(self):
        """
        Determines if player can move west.

        @return:    True if possible, false otherwise.
        """
        exit = self._location.getExit(constants.Direction.WEST)

        if exit:
            return True
        return False


    def moveNorth(self):
        """
        Moves player north one space.
        """
        northSpace = self._location.getExit(constants.Direction.NORTH) 
        
        #If north space does not exist, do nothing
        if not northSpace:
            return
        #..otherwise, move to new space 
        self._location = northSpace

    def moveSouth(self):
        """
        Moves player south one space.
        """
        southSpace = self._location.getExit(constants.Direction.SOUTH)

        #If south space does not exist, do nothing
        if not southSpace:
            return
        #..otherwise, move to new space 
        self._location = southSpace 

    def moveEast(self):
        """
        Moves player east one space.
        """
        eastSpace = self._location.getExit(constants.Direction.EAST)

        #If east space does not exist, do nothing
        if not eastSpace:
            return
        #..otherwise, move to new space 
        self._location = eastSpace 

    def moveWest(self):
        """
        Moves player west one space.
        """
        westSpace = self._location.getExit(constants.Direction.WEST)

        #If west space does not exist, do nothing
        if not westSpace:
            return
        #..otherwise, move to new space 
        self._location = westSpace 

    def getLocation(self):
        """
        Returns player's current location (i.e. space).

        @return:    Player's current location.
        """
        return self._location
