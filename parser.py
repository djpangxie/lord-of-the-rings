#!/usr/bin/python

import constants


class Parser(object):
    """
    解析用户输入，搜索已注册的命令。
    """

    def __init__(self, commandWords):
        """
        初始化解析器。

        @param commandWords:     命令字典
        """
        if not commandWords:
            errorMsg = "解析器必须用CommandWords对象进行初始化。"
            raise AssertionError(errorMsg)

        self._commandWords = commandWords

    def getNextCommand(self):
        """
        获取用户的下一条命令。
        """
        userInput = input(constants.COMMAND_PROMPT)
        userInput = userInput.strip().lower()

        while not self._commandRecognized(userInput):
            print("命令 %s 无法识别。键入 help 查看帮助" % userInput)
            print("")

            userInput = input(constants.COMMAND_PROMPT)
            userInput = userInput.strip().lower()

        command = self._commandWords.getCommand(userInput)
        return command

    def _commandRecognized(self, name):
        """
        判断用户输入的是否是已注册的命令。

        @param name:        命令的名称
        @return:            如果识别到该命令则为True，否则为False
        """
        # 确保名称不是None
        if not name:
            return False

        recognized = self._commandWords.isCommand(name)
        return recognized
