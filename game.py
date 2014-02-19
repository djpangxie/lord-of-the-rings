#!/usr/bin/python

from parser import Parser
from commands.commandwords import CommandWords
from commands.helpcommand import HelpCommand 
from commands.quitcommand import QuitCommand
from commands.dropcommand import DropCommand
from commands.pickupcommand import PickUpCommand
from player import Player
from worldmap import WorldMap

class Game(object):
    """
    Prepares and executes turn-based game.
    """

    def __init__(self):
        """
        Initializes new game.
        """
        
        #Player
        self._player = Player()

        #World Map
        self._worldMap = WorldMap()
        
        #CommandWords
        self._commandWords = CommandWords()

        #Commands
        helpCmd = HelpCommand("help", 
                    "Provides help information for game.", self._commandWords)
        self._commandWords.addCommand("help", helpCmd)

        quitCmd = QuitCommand("quit", "Exits the game.")
        self._commandWords.addCommand("quit", quitCmd)
        
        ##Need to create board##
        dropCmd = DropCommand("drop", "Drops an item from inventory into location.", self._player, self._board)
        self._commandWords.addCommand("drop", dropCmd)

        pickupCmd = PickUpCommand("pick up", "Picks up an item from a location and adds to inventory.")
        self._commandWords.addCommand("pick up", pickupCmd)
    
        #Parser
        self._parser = Parser(self._commandWords)

    def play(self):
        """
        Executes main game loop.
        """
        print "Welcome to Lord of the Rings Adventure Game!"
        print "(Type 'help' for a list of available commands)"
        print ""

        while(True):
            self._nextTurn()

    def _nextTurn(self):
        """
        Executes next turn.
        """
        nextCommand = self._parser.getNextCommand()
        
        if nextCommand is not None:
            nextCommand.execute()
            print ""
        else:
            errorMsg = "Failed to received command from parser."
            raise AssertionError(errorMsg)
