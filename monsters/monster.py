#!/usr/bin/python

import constants
import random


class Monster(object):
    """
    一个通用怪物类，用作特定怪物子类的父类。
    """

    def __init__(self, name, description, stats, attackString, deathString):
        """
        初始化怪物对象。

        @param name:          怪物名称
        @param description:   怪物的描述
        @param stats:         怪物基础数据的三元列表，包括最大生命值、攻击力和经验值（按此顺序）
        @param attackString:  怪物攻击时显示的字符串。例如：“迈尔斯非常生气，开始四处冲锋。”
        @param deathString:   怪物死亡时显示的字符串。例如：“迈尔斯认为他受够了，就回家了。”
        """
        self._name = name
        self._description = description
        self._stats = stats
        self._hp = stats[0]
        self._attack = stats[1]
        self._experience = stats[2]
        self._attackString = attackString
        self._deathString = deathString

    def getName(self):
        """
        获取怪物名称。

        @return: 怪物名称
        """
        return self._name

    def getDescription(self):
        """
        获取怪物的描述。

        @return: 怪物的描述
        """
        return self._description

    def getHp(self):
        """
        获取怪物的HP
        
        @return: 怪物的HP
        """
        return self._hp

    def attack(self, target):
        """
        攻击给定目标。

        @param target:   攻击的目标对象

        @return:         实际对目标造成的伤害(正态波动)
        """
        damage = random.normalvariate(self._attack, self._attack / constants.BattleEngine.ATTACK_VOLATILITY)
        damage = max(int(damage), 0)
        return target.takeAttack(damage)

    def getAttack(self):
        """
        获取怪物的攻击力。
        
        @return: 怪物的攻击力
        """
        return self._attack

    def takeAttack(self, attack):
        """
        受到伤害。注意HP不能小于零。

        @param attack: 受到的攻击量
        """
        self._hp = max(self._hp - attack, 0)

    def recoverHp(self):
        """
        将怪物的生命恢复到初始最大值
        """
        self._hp = self._stats[0]

    def getExperience(self):
        """
        获取怪物的经验值。

        @return: 怪物的经验值
        """
        return self._experience

    def getAttackString(self):
        """
        获取怪物攻击时显示的字符串。

        @return: 怪物攻击时显示的字符串
        """
        return self._attackString

    def getDeathString(self):
        """
        获取怪物死亡时显示的字符串。

        @return: 怪物死亡时显示的字符串
        """
        return self._deathString
