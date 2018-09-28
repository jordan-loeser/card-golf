#!/usr/bin/env python3

import settings

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.faceUp = False

    def getSuit(self):
        """
        getFaceValue(): returns the human-readable suit value
        """
        val = self.suit
        suits = {
            0: '♤',
            1: '♧',
            2: '♡',
            3: '♢',
        }
        return suits.get(val, -1)

    def getFaceValue(self):
        """
        getFaceValue(): returns the human-readable face value
        """
        val = self.value
        if(val > 1 and val < 11):
            return str(val) + (' ', '')[val == 10]
        faces = {
            1:  'A ',
            11: 'J ',
            12: 'Q ',
            13: 'K ',
        }
        return faces.get(val, -1)

    def flipUp(self):
        """
        faceUp(): flips a card so the value is showing
        """
        self.faceUp = True

    def flipDown(self):
        """
        faceDown(): hides the value from view
        """
        self.faceUp = False
