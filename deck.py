#!/usr/bin/env python3

import random
from card import Card

class Deck:

    def __init__(self):
        self.cards = []

    def fillDeck(self):
        """
        fillDeck(): creates a standard 52-card Deck
        """
        self.cards = []
        for suit in range(4):
            for val in range(1, 14):
                self.cards.append(Card(suit, val))

    def getCard(self, index):
        curCard = self.cards[index]
        return curCard.getFaceValue() + ' of ' + curCard.getSuit()

    def addCard(self, newCard):
        self.cards.append(newCard)

    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        card = self.cards.pop()
        return card
