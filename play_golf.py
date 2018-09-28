#!/usr/bin/env python3
"""
Play_Golf.py: Initiates a game of 6-card golf
"""

__author__ = "Jordan Loeser"
__email__ = "loeser.jordan@gmail.com"

import curses
import settings
from game import Game

def main(stdscr):
    """
    main(): Controls the UI and Gameplay
    """
    # Clear screen
    stdscr.clear()
    stdscr.keypad(True)

    # Initialize Windows
    settings.init()

    # Run the game until [ctr-c] is pressed
    while True:
        game = Game()
        game.playGolf()

curses.wrapper(main) # Facilitate curses setup and teardown
