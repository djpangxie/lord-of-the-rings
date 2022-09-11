#!/usr/bin/python

from constants import LEVEL_EXP_REQUIREMENT
from constants import MAX_LEVEL
from items.armor import Armor
from items.weapon import Weapon
from .command import Command


class CheckStatsCommand(Command):
    """
    显示玩家统计数据。
    """

    def __init__(self, name, explanation, player):
        """
        初始化新的检查统计命令。

        @param name:         命令名称
        @param explanation:  命令的说明
        @param player:       玩家对象
        """
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        显示玩家状态。
        """
        # 获取玩家数据
        name = self._player.getName()
        experience = self._player.getExperience()
        weightLimit = self._player.getWeightLimit()
        level = self._player.getLevel()
        nextlevel = level + 1
        if nextlevel > MAX_LEVEL:
            nextlevel = 1

        # 获取HP数据
        hp = self._player.getHp()
        maxhp = self._player.getMaxHp()
        charmHp = self._player.getCharmHp()
        totalMaxHp = self._player.getTotalMaxHp()

        # 获取攻击数据
        attack = self._player.getAttack()
        charmAttack = self._player.getCharmAttack()
        totalAttack = self._player.getTotalAttack()

        # 获取防御数据
        charmDefense = self._player.getCharmDefense()
        totalDefense = self._player.getTotalDefense()

        # 创建默认值 - 用于确定武器和盔甲是否存在
        weapon = None
        armor = None

        # 获得装备加值信息
        equipment = self._player.getEquipped()
        equipmentList = equipment.getItems()
        for item in equipmentList:
            if isinstance(item, Weapon):
                weaponsAttack = item.getAttack()
                weapon = True
            if isinstance(item, Armor):
                armorDefense = item.getDefense()
                armor = True

        # 打印数据
        print("%s的当前状态：\n" % name)
        print("\tHP：%s/%s\t\t负重：%s/%s\t\t等级：%s\t\t经验值：%s/%s" % (
            hp, totalMaxHp, self._player.getInventory().getWeight(), weightLimit, level, experience,
            LEVEL_EXP_REQUIREMENT[nextlevel]))
        print("\t攻击力：%-6s（基础攻击力：%-5s武器攻击力：%-5s总饰品攻击加值：%s）" % (
            totalAttack, attack, weaponsAttack if weapon else 0, charmAttack))
        print("\t防御力：%-6s（盔甲防御力：%-5s总饰品防御加值：%s）" % (
            totalDefense, armorDefense if armor else 0, charmDefense))
        print("\t最大HP：%-6s（基础最大HP：%-5s总饰品最大HP加值：%s）" % (totalMaxHp, maxhp, charmHp))
