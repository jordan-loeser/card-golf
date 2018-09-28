#!/usr/bin/env python3
"""
Settings.py: Initiates a game of 6-card golf
"""
import curses

def init():
    # Create Two Screens
    scoreboardHeight = 5
    global mainscreen, scoreboard
    mainscreen = curses.newwin(curses.LINES - scoreboardHeight, curses.COLS, scoreboardHeight, 0)
    scoreboard = curses.newwin(scoreboardHeight, curses.COLS, 0, 0)

    # Set Window Background Colors
    if curses.can_change_color():
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_GREEN)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_GREEN)
        mainscreen.bkgd(' ', curses.color_pair(1))
        scoreboard.bkgd(' ', curses.color_pair(2))
        mainscreen.refresh()
        scoreboard.refresh()

# Graphic Utilty Functions

def buildLogo():
    lines = [
        "  ___ __ _ _ __ __| | __ _  ___ | |/ _|",
        " / __/ _` | '__/ _` |/ _` |/ _ \| | |_ ",
        "| (_| (_| | | | (_| | (_| | (_) | |  _|",
        " \___\__,_|_|  \__,_|\__, |\___/|_|_|  ",
        "                     |___/             ",
    ]
    lines = [line.center(curses.COLS - 1) for line in lines]
    return '\n'.join(lines)

def displayCard(y, x, card, label=""):
    """
    displayCard(): prints the card at the given location
    """
    # Hide card if it is face down
    if not(card.faceUp):
        cardToShow = ['┌───────────┐'] + (['│░░░░░░░░░░░│'] * 6) + ['└───────────┘']
    # Show card if it is face up
    else:
        cardToShow = ['┌───────────┐'] + ['│' + card.getSuit() + ' ' + card.getFaceValue() + '       │'] + ['│           │'] + (['│           │'] * 3) + ['│         🏌 ️│'] + ['└───────────┘']

    for i in range(8):
        mainscreen.addstr(y+i, x, cardToShow[i], curses.color_pair(3))

    if not(len(label) == 0): mainscreen.addstr(y+8, x, label)

    mainscreen.refresh()
    return
