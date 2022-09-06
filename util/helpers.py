#!/usr/bin/python

def generateMenu(prompt, options, appendQuit=False):
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
    # 导入模块
    from items.weapon import Weapon
    from items.armor import Armor
    from items.charm import Charm
    from items.potion import Potion
    from items.item import Item

    # 创建变量
    itemslist = itemSet.getItems()
    weaponitems = []
    armoritems = []
    charmitems = []
    potionitems = []
    otheritems = []

    # 分门别类
    for item in itemslist:
        if isinstance(item, Weapon):
            weaponitems.append(item)
        elif isinstance(item, Armor):
            armoritems.append(item)
        elif isinstance(item, Charm):
            charmitems.append(item)
        elif isinstance(item, Potion):
            potionitems.append(item)
        else:
            otheritems.append(item)

    itemslist.clear()
    itemslist.extend(weaponitems)
    itemslist.extend(armoritems)
    itemslist.extend(charmitems)
    itemslist.extend(potionitems)
    itemslist.extend(otheritems)


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
