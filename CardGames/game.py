from player import Player
from deck import Deck
from pile import Pile

"""This defines the game class """

class Game:

    #gameName will be the name of the game
    #players will be a string of player IDs
    
    def __init__(self, gameName, players, numPlayers):
        self.name = gameName
        # self.currentState = startState
        self.players = [Player(p) for p in players]
        self.winner = None
        self.currentPlayer = None
        self.numPlayers = numPlayers
        self.currentTurn = 0
        self.createDeck()
        self.createPile()

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
        return self.numPlayers

    def playerTurn(self):
        return self.numPlayers - self.currentTurn

    def createDeck(self):
        self.deck = Deck()
        self.deck.shuffle()

    def createPile(self):
        self.pile = Pile()
        self.deck.shuffle()
        self.setTopCard(self.pile.getFirstCard)
        self.setSecondCard(self.pile.getSecondCard)
        self.setThirdCard(self.pile.getThirdCard)
