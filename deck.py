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

    def addCard(self, newCard):
        """
        addCard(): appends a Card to the deck
        """
        self.cards.append(newCard)

    def shuffle(self):
        """
        shuffle(): randomly shuffles the deck
        """
        random.shuffle(self.cards)

    def drawCard(self):
        """
        drawCard(): returns and removes the top card of the deck
        """
        card = self.cards.pop()
        return card
