import Player, Deck, abstractmethod

"""This defines the game class """

class Game:

    #gameName will be the name of the game
    #players will be a string of player IDs
    
    def __init__(self, gameName, players):
        self.name = gameName
        self.currentState = startState
        self.players = [Player(p) for p in players]
        createDeck()

    def setTopCard(self, topCard):
        self.topCard = topCard

    def setCurrentPlayer(self, currentPlayer):
        self.currentPlayer = (Player) currentPlayer

    def setCurrentState(self, state):
        self.currentState = state;

    def getCurrentState(self):
        return self.currentState

    def getCurrentPlayer(self):
        return self.currentPlayer

    def setWinner(self, winner):
        self.winner = (Player) winner

    def runGame(self):
        #custom to each game

    def createDeck(self):
        self.deck = Deck()
    

""" This defines the abstract state class 
    (we can just put these within the custom implementations)"""

    class State:

        def __init__(self, stateName):
            self.stateName = stateName

        def setNextState( self, state):
            setCurrentState(state)

        def processCurrent(self):
            #custom to state

    class Begin(State, firstPlayer):

        def setNextState(self, state):
            #custom to game
        
        def processCurrent(self, firstPlayer):
            setCurrentPlayer(firstPlayer)

    class End(State):
        
        def setWinningPlayer(self):
            setWinner(getCurrentPlayer())
        
        def processCurrent(self) 
            setWinner()
        
        def setNextState(self):
            #nothing

        
        

    
        
    