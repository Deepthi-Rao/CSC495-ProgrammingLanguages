from Player import Player
from Deck import Card, Deck
from Hand import Hand

"""This defines the game class """

class Game:

    #gameName will be the name of the game
    #players will be a string of player IDs
    
    def __init__(self, gameName, players):
        self.name = gameName
        # self.currentState = startState
        self.players = [Player(p) for p in players]
        self.winner = None
        self.currentPlayer = None

    def setTopCard(self, topCard):
        self.topCard = topCard

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

    def createDeck(self):
        self.deck = Deck()
        self.deck.shuffle()
    

""" This defines the abstract state class 
    (we can just put these within the custom implementations)"""

class State:

    def __init__(self, stateName):
        self.stateName = stateName

    def setNextState( self, state):
        setCurrentState(state)

    def processCurrent(self):
        #custom to state
        return

class Begin(State):

    def setNextState(self, state):
        #custom to game
        return
    
    def processCurrent(self, firstPlayer):
        setCurrentPlayer(firstPlayer)

class End(State):
    
    def setWinningPlayer(self):
        setWinner(getCurrentPlayer())
    
    def processCurrent(self):
        setWinner()
    
    def setNextState(self):
        #nothing
        return

        
        

    
        
    