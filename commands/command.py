#!/usr/bin/python

class Command(object):
    """
    所有 Command 对象的父类。
    """

    def __init__(self, name, explanation, time=False):
        """
        初始化新的命令对象。

        @param name:          命令名称
        @param explanation:   命令的说明
        @param time:          如果该命令会造成时间流逝则为True，否则为False
        """
        self._name = name
        self._explanation = explanation
        self._time = time

    def getName(self):
        """
        返回命令名称。
        
        @return:    命令名称
        """
        return self._name

    def getExplanation(self):
        """
        返回命令的说明。
        
        @return:    命令的说明
        """
        return self._explanation

    def getTime(self):
        """
        如果该命令会造成时间流逝则返回True，否则返回False。

        @return:   如果该命令会造成时间流逝则为True，否则为False
        """
        return self._time

    def execute(self):
        """
        默认执行方法。默认情况下，什么都不做。

        这个方法应该被子类重写。
        """
        pass
