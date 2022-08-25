#!/usr/bin/python

from .command import Command
import constants


class QuitCommand(Command):
    """
    退出命令。
    """

    def __init__(self, name, explanation):
        """
        初始化退出命令。

        @param name:          命令名称
        @param explanation:   命令的说明
        """
        Command.__init__(self, name, explanation)

    def execute(self):
        """
        运行退出命令。
        """
        # 确认退出
        response = input("你确定你要退出吗？(yes/no): ")
        response = response.strip().lower()

        if 'yes' in response:
            print("退出....")
            exit(0)
