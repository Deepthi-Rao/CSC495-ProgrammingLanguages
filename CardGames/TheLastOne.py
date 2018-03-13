from Game import Game
from Player import Player
from Deck import Card, Deck
from Hand import Hand

class TheLastOne(Game):
    def __init__(self, players, handSize=6):
        self.name = "The Last One"
        self.handSize = handSize
        self.players = players
        self.currentPlayer = None
        
        
    def runGame(self):
        theDeck = Deck(True)
        theDeck.shuffle()
        for p in self.players:
            cards = theDeck.deal(self.handSize)
            hand = Hand(cards, self.handSize)
            p.setHand(hand)
        

players = [Player("H"), Player("R"), Player("Q")]
print(players)

game = TheLastOne(players)
game.runGame()
players[0].viewHand()
players[1].viewHand()


