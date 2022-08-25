#!/usr/bin/python

class CommandWords(object):
    """
    游戏中使用的所有命令对象的字典。
    """

    def __init__(self):
        """
        初始化新的命令字典。
        """
        self._commandWords = {}

    def addCommand(self, name, command):
        """
        将命令添加到命令字典。

        @precondition:      命令名称尚未分配。

        @param name:        命令名称
        @param command:     命令对象
        """
        # 命令是否已经存在？
        if self.isCommand(name):
            errorMsg = "无法添加 '%s' 命令；该命令名称已在使用中。" % name
            raise AssertionError(errorMsg)

        # 添加命令
        self._commandWords[name] = command

    def getCommand(self, name):
        """
        按名称检索命令。

        @precondition:      命令已注册

        @param name:        命令名称
        @return:            命令对象。如果未找到命令，则返回None
        """
        if self.isCommand(name):
            return self._commandWords[name]

        return None

    def getCommandNames(self):
        """
        返回所有命令名称的列表。

        @return:            所有命令名称的列表
        """
        names = list(self._commandWords.keys())
        names.sort()

        return names

    def removeCommand(self, name):
        """
        按名称删除命令。

        @precondition:      命令已注册

        @param name:        命令名称
        """
        if not self.isCommand(name):
            errorMsg = ("无法从字典中删除 '%s' 命令；识别不到该命令。" % name)
            raise AssertionError(errorMsg)
        del self._commandWords[name]

    def isCommand(self, name):
        """
        判断字典中是否已定义了具有给定名称的命令。

        @param name:    命令名称
        @return:        如果命令已定义则为True，否则为False
        """
        exists = name in list(self._commandWords.keys())
        return exists
