from player import Player
from deck import Card, Deck
from hand import Hand
from pile import Pile

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
        createPile()

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

    def createPile(self):
        self.pile = Pile()
        self.deck.shuffle()
        setTopCard(self.pile.getFirstCard)
        setSecondCard(self.pile.getSecondCard)
        setThirdCard(self.pile.getThirdCard)
