#!/usr/bin/python

from cities.building import Building
from items.item import Item

class Square(Building):
    """
    广场派生于建筑，并位于城市之中。
    广场作为公共空间，让玩家可以与城里人交流。
    """
    def __init__(self, name, description, greetings, talk = None, items = None):
        """
        初始化广场对象。

        @param name:           广场名称
        @param description:    广场的描述
        @param greetings:      玩家进入广场时得到的问候
        @param talk:           用于对话的 人名-对话 的字典
        @param items:          玩家与人交谈可能会收到的物品
        """
        Building.__init__(self, name, description, greetings)

        self._talk = talk
        self._items = items
        
    def enter(self, player):
        """
        The action sequence for square.
        
        @param player:     The player object.
        """
        print("")
        print("- - - %s - - -" % self._name)
        print(self._greetings)
        print("")

        #If square is empty
        if self._talk == None:
            print("You find %s completely deserted." % self._name)
            return

        #User prompt
        numPeople = len(self._talk)
        
        choice = None
        while choice != "quit":
            print("There are %s people to talk to in %s:" % (numPeople, 
            self._name))
            for person in self._talk:
                print("\t %s" % person)

            prompt = "\nWhom would you like to talk to ('quit' to quit)? "
            choice = input(prompt)

            #The option to leave
            if choice == "quit":
                print("Leaving %s." % self._name)

            #If person exists
            elif choice in self._talk:
                print("")
                print("\"%s\"" %  self._talk[choice])

                #If target person has items
                if choice in self._items:
                    print("")
                    gift = self._items[choice]
                    self._giveItem(player, choice)
                    
            #If person doesn't exist
            else:
                print("")
                print("Alas, '%s' could not be found in %s." % (choice, 
                self._name))
     
            input("\nPress enter to continue. ")
            print("")
            
    def _giveItem(self, player, choice):
        """
        Helper method that is responsible for handing player receiving items.
        
        @param player:  The player object.
        @param gift:    The gift that player is supposed to receive.
        @param choice:  The person that the user has chosen to talk to.
        """
        gift = self._items[choice]
        
        #If entry is single item
        if isinstance(gift, Item):
            print("%s gave %s to %s." % (choice, gift.getName(),
                player.getName()))
            if player.addToInventory(gift):
                del self._items[choice]
            
        #If entry is a list
        elif isinstance(gift, list):
            successfulItems = []
            for item in gift:
                print("%s gave %s to %s." %(choice, item.getName(),
                     player.getName()))
                if player.addToInventory(item):
                    successfulItems.append(item)
                    
            #Cleanup
            if successfulItems == gift:
                del self._items[choice]
            for item in successfulItems:
                gift.remove(item)
