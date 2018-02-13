#!/usr/local/bin/python3

import sys, traceback, time, random

class Deck:
    def __repr__(self):
        return self.__class__.__name__
        
    def __init__(self, jokers=False):
        suits = ["hearts","diamonds","spades","clubs"]
        ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        if jokers:
            self.cards.append(Card(None, "joker"))
            self.cards.append(Card(None, "joker"))
            
    def shuffle(self):
        return

class Card:
    def __repr__(self):
        return self.__class__.__name__
        
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def getSuit(self):
        return self.suit
        
    def getRank(self):
        return self.rank
        
class Hand:
    def __repr__(self):
        return self.__class__.__name__
        
class Game:
    def __repr__(self):
        return self.__class__.__name__
        
    def deal(self):
        return
        
