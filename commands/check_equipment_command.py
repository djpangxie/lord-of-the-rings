#!/usr/bin/python

from .command import Command
from items.weapon import Weapon
from items.armor import Armor
from items.charm import Charm


class CheckEquipmentCommand(Command):
    """
    显示玩家装备和详细的装备统计信息。
    """

    def __init__(self, name, explanation, player):
        """
        初始化新的检查装备命令。

        @param name:         命令名称
        @param explanation:  命令的说明
        @param player:       玩家对象
        """
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        显示玩家装备栏中的物品。
        """
        playerName = self._player.getName()
        equipment = self._player.getEquipped()

        # 打印当前装备的物品
        print("%s 当前装备的物品：\n" % playerName)

        for item in equipment:
            itemName = item.getName()
            if isinstance(item, Weapon):
                attack = item.getAttack()
                print("\t武器：%s" % itemName)
                print("\t%s的攻击力为 %s 点" % (itemName, attack))
            elif isinstance(item, Armor):
                defense = item.getDefense()
                print("\t盔甲：%s" % itemName)
                print("\t%s的防御力为 %s 点" % (itemName, defense))
            elif isinstance(item, Charm):
                attack = item.getAttack()
                defense = item.getDefense()
                hp = item.getHp()
                print("\t饰品：%s:" % itemName)
                if item.getAttack():
                    print("\t%s有 %s 点攻击加值" % (itemName, attack))
                if item.getDefense():
                    print("\t%s有 %s 点防御加值" % (itemName, defense))
                if item.getHp():
                    print("\t%s有 %s 点最大生命加值" % (itemName, hp))
            else:
                errorMsg = "某件装备的类型不是武器、盔甲或饰品！"
                raise AssertionError(errorMsg)
            print("")
