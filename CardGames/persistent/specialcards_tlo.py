#!/usr/local/bin/python3

import sys, traceback, time, random

class SpecialCard:
    def onNextCard(self, nextCard):
        return
    
class TwoCard(SpecialCard):
    def __repr__(self):
        "The next player must draw two cards from the stock, and is not allowed to play a card."
    
class ThreeCard(SpecialCard):
    def __repr__(self):
        "The current player may play any card on top of this card."
        
class FourCard(SpecialCard):
    def __repr__(self):
        "Melee. If the next player (or any other player) has the next rank card of the same suit, they may play it. If no one plays the next card, the next player must draw from stock the number of cards equal to the value of the current card."
        
class EightCard(SpecialCard):
    def __repr__(self):
        "The current player announces a suit, and the next play should be in the announced suit."
        
class JackCard(SpecialCard):
    def __repr__(self):
        "The next player skips a turn."
        
class AceCard(SpecialCard):
    def __repr__(self):
        "The direction of play is now reversed."
        
class JokerCard(SpecialCard):
    def __repr__(self):
        "The Joker can represent any card of the pack, at the choice of the current player."