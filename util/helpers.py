#!/usr/bin/python

def generateMenu(prompt, options, appendQuit = False):
    """
    Generates menus and solicit and returns user choice.

    @param prompt:       User prompt. For example: "You are in the store."
    @param options:      List of options, stored as strings.
    @param appendQuit:   Whether there should be the option to quit.
    
    @return:             User choice.
     """
    print(prompt)
    print("")

    if appendQuit:
        options.append("Quit")

    index = 1
    for option in options:
        print("%s)\t%s" % (str(index), option)) 
        index += 1

    choice = input("Choice: ")

    return choice

def sortItems(itemSet):
    """
    对 ItemSet 中的物品进行排序。

    @param itemSet:   待排序的ItemSet对象
    """
    #导入模块
    from items.weapon import Weapon
    from items.armor import Armor
    from items.charm import Charm
    from items.potion import Potion
    from items.item import Item
    
    #创建变量
    itemsList = itemSet.getItems()
    sortedItems = []
    
    charms = {}
    charmNames = []
    potions = {}
    potionNames = []
    items = {}
    itemNames = []
    
    #武器排第一
    for item in itemsList:
        if isinstance(item, Weapon):
            sortedItems.append(item)
            itemsList.remove(item)
    
    #盔甲排第二
    for item in itemsList:
        if isinstance(item, Armor):
            sortedItems.append(item)
            itemsList.remove(item)
            
    #接着按名称排序饰品
    for item in itemsList:
        if isinstance(item, Charm):
            charmName = item.getName()
            charmNames.append(charmName)
            charms[charmName] = item
            itemsList.remove(item)
            
    #再接着按名称排序药水
    for item in itemsList:
        if isinstance(item, Potion):
            potionName = item.getName()
            potionNames.append(potionName)
            potions[potionName] = item
            itemsList.remove(item)
            
    #剩下的物品放最后
    for item in itemsList:
        itemName = item.getName()
        itemNames.append(itemName)
        items[itemName] = item
        
    charmNames.sort()
    for charmName in charmNames:
        sortedItems.append(charms[charmName])

    potionNames.sort()
    for potionName in potionNames:
        sortedItems.append(potions[potionName])
        
    itemNames.sort()
    for itemName in itemNames:
        sortedItems.append(items[itemName])
        
    itemSet.clearItems()
    itemSet.addItems(sortedItems)
    
def triangular(stats):
    """
    使用三角分布生成一个随机数。
    
    @param stats:   一个三元素列表，其元素用于计算三角分布
    
    @return:        随机生成的数字
    """
    import random
    
    low = stats[0]
    high = stats[1]
    mode = stats[2]
    
    u = random.random()
    try:
        if mode is None:
            c = 0.5  
        else:
            c = (mode - low) / (high - low)
    except ZeroDivisionError:
        return low
        
    if u > c:
        u = 1.0 - u
        c = 1.0 - c
        low, high = high, low
        
    return low + (high - low) * (u * c) ** 0.5