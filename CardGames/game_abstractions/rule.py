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

    def __init__(self, msg, player, card, subCard, numTokens, Game):
        self.msg = msg
        self.player = player
        self.card = card
        self.subCard = subCard
        self.numTokens = numTokens
        self.game = Game

