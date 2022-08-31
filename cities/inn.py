#!/usr/bin/python

from cities.building import Building
import constants

class Inn(Building):
    """
    旅店派生自建筑。
    旅店是允许玩家有偿治疗的建筑地点。
    """
    def __init__(self, name, description, greetings, cost):
        """
        初始化旅店

        @param name:         旅店的名字
        @param description:  旅店的描述
        @param greetings:    玩家进入旅店时得到的问候
        @param cost:         使用旅店的费用
        """
        Building.__init__(self, name, description, greetings)
        
        self._cost = cost
        
    def enter(self, player):
        """
        The action sequence upon player entering inn.
        
        @param player:     The player object.
        """
        cost = self.getCost()

        print("")
        print("- - - %s - - -" % self.getName())
        print(self._greetings)
        print("Cost to stay: %s." % cost)

        #Determine player choice
        choice = None
        while choice != "no":
            print("")
            choice = input("Would you like to stay for the night?" 
            " Response: 'yes' or 'no.' ")
            
            #Heal option   
            if choice == "yes":
                #Money check and transfer
                if player.getMoney() >= cost:
                    player.decreaseMoney(cost)
                    #Actual healing operation
                    self._heal(player)
                    print("%s was healed at %s cost! %s has %s%s remaining." \
                          % (player.getName(), cost, player.getName(), 
                          player.getMoney(), constants.CURRENCY))
                #Not enough money
                else:
                    print("%s doesn't have enough money." % player.getName())
                input("Press enter to continue. ")
                return
                
            #Non-use option
            elif choice == "no":
                print("Thanks for coming to %s." % self._name)
                input("Press enter to continue. ")
                
            #For invalid input
            else:
                print("'What?'")
    
    def getCost(self):
        """
        返回旅店的费用。
        
        @return:    一个整数值表示的使用旅店的花费
        """
        return self._cost

    def _heal(self, player):
        """
        治愈玩家至最大生命值。

        @param player:    玩家对象
        """
        maxHp = player.getMaxHp()
        hp = player.getHp()
        amountToHeal = maxHp - hp

        player.heal(amountToHeal)