from Game import Game
from Player import Player
from Deck import Card, Deck
from Hand import Hand

class State():
    def __repr__(self):
        return self.__class__.__name__
        
class BeginState(State):
    def __repr__(self):
        return self.__class__.__name__
        
class TurnState(State):
    def __repr__(self):
        return self.__class__.__name__ 
        
    def __init__(self):
        self.id = None
    
    def setId(self, player):
        self.id = player

class TheLastOne(Game):
    
    def __init__(self, players, handSize=6):
        BEGIN = BeginState()
        TURN = TurnState()
        self.name = "The Last One"
        self.handSize = handSize
        self.players = players
        self.currentPlayer = None
        self.currentState = BEGIN
        self.numTurns = len(players)
        self.turns = []
        
    def runGame(self, handSize=6):
        if handSize < 4 or handSize > 8:
            print("Invalid hand size. Using default setting.")
        else:
            self.handSize = handSize
        theDeck = Deck(True)
        theDeck.shuffle()
        for p in self.players:
            cards = theDeck.deal(self.handSize)
            hand = Hand(cards, self.handSize)
            p.setHand(hand)
            turn = TurnState()
            turn.setId(p.getId)
            self.turns.append(turn)
        
    def pickCard(self, player, cardString):
        cards = player.hand.getCardsInHand()
        if cardString.lower() == "joker":
            joker = Card(None, "joker")
            for card in cards:
                if card.match(joker):
                    return "joker"
                
            return "sad"
            

        

players = [Player("H"), Player("R"), Player("Q")]
print(players)

game = TheLastOne(players)
game.runGame(8)
players[0].viewHand()
players[1].viewHand()
print(game.pickCard(players[0], "joker"))

