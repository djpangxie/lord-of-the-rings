#!/usr/bin/python

from .command import Command


class HelpCommand(Command):
    """
    帮助命令。
    """

    def __init__(self, name, explanation, commandWords):
        """
        初始化帮助命令。

        @param name:                命令名称
        @param explanation:         命令的说明
        @param commandWords:        游戏中使用的命令字典
        """
        Command.__init__(self, name, explanation)

        self._commandWords = commandWords

    def execute(self):
        """
        运行帮助命令。
        """
        # 打印页眉
        print("在游戏过程中可以使用以下命令：")

        # 打印每个已定义命令的名称及其说明
        words = self._commandWords

        names = words.getCommandNames()
        for name in names:
            command = words.getCommand(name)
            explanation = command.getExplanation()
            print("%-20s%s" % (name, explanation))
