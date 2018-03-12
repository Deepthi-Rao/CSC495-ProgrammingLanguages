from Player import Player
from Deck import Card, Deck
from Hand import Hand

"""This defines the game class """

class Game:

    #gameName will be the name of the game
    #players will be a string of player IDs
    
    def __init__(self, gameName, player, numPlayers):
        self.name = gameName
        # self.currentState = startState
        self.players = [Player(p) for p in players]
        self.winner = None
        self.currentPlayer = None
        createDeck()

    def setTopCard(self, topCard):
        self.topCard = topCard

    def setSecondCard(self, secondCard):
        self.secondCard = secondCard
    
    def setThirdCard(self, thirdCard):
        self.thirdCard = thirdCard
    
    def getTopCard(self):
        return self.topCard
    
    def getSecondCard(self):
        return self.secondCard

    def getThirdCard(self):
        return self.thirdCard

    def setCurrentPlayer(self, currentPlayer):
        self.currentPlayer = currentPlayer

    def setCurrentState(self, state):
        self.currentState = state;

    def getCurrentState(self):
        return self.currentState

    def getCurrentPlayer(self):
        return self.currentPlayer

    def setWinner(self, winner):
        self.winner = winner

    def runGame(self):
        #custom to each game
        return

    def getPlayerCount(self):
        return numPlayers

    def playerTurn(self):
        return numPlayers - turn

    def createDeck(self):
        self.deck = Deck()
        self.deck.shuffle()
        setTopCard(self.deck.getFirstCard)
        setSecondCard(self.deck.getSecondCard)
        setThirdCard(self.deck.getThirdCard)
    

""" This defines the abstract state class 
    (we can just put these within the custom implementations)"""


#might be useful to have in the larger game class
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

        
        

    
        
    