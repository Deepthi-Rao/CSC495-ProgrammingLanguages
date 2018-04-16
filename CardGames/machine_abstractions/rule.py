#This is the rules class that defines the properties of a rule

from game_abstractions.game import Game

class Rule:

    # this defines a rules with a player and a message
    def __init__(self, Game):
        self.game = Game;

    # this defines a rules with a player and a message
    def __init__(self, msg, player):
        self.msg = msg
        self.player = player

    # this defines a rules with just a player
    def __init__(self, player):
        self.player = player

    #This checks to see if the card is
    def cardIs(card, *, rank=None, suit=None):
        if not rank and not suit:
            raise Exception("Invalid isCard use. Must define rank or suit.")
        if rank and not card.getRank() == rank:
            return False
        if suit and not card.getSuit() == suit:
            return False
        return True


    #This checks the rank or the suit
    def cardRankOrSuitIs(card, *, rank=None, suit=None):
        if not rank or not suit:
            raise Exception('Invalid cardRankOrSuitIs use. Should use isCard for single checks.')
        if cardIs(card, rank=rank) or cardIs(card, suit=suit):
            return True
        return False

    #gets the first word of the message for the rule
    def firstWord(msg):
        return msg.split()[0].upper()

    #Checks if the player can play