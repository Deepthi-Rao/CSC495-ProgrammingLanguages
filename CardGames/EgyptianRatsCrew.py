from Game import Game
from Player import Player
from Deck import Card, Deck
from Hand import Hand
from Pile import Pile
"""TODO:make a pile and move all some deck functions into pile
        make it so that each player plays their top card
        check if slappable or not
        check if deck has zero cards and each player has zero card game ends"""
#gameName will be the name of the game
#players will be a string of player IDs
class EgyptianRatsCrew(Game):
    
    def __init__(self, playersID):
        self.name = "Egyptian Rats Crew"
        self.players = [Player(p) for p in playersID]
        self.numPlayers = len(self.players)
        if(52 % self.numPlayers == 0):
            self.handSize = 52 % self.numPlayers

        #else: #handles over flow cards
            #redistribute()
            
        self.currentPlayer = self.players[0] #first entered is the first player
        self.currentState = Begin(self)
        self.turn = self.numPlayers - 1
        self.pile = []
        self.createDeck()
        self.createPile()
    
    def getPile(self):
        return self.pile

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

    def getPlayerCount(self):
        return 

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

    def setCurrentPlayer(self):
        self.currentPlayer = self.players[self.turn]

    def setCurrentState(self, state):
        self.currentState = state;

    def getCurrentState(self):
        return self.currentState

    def getCurrentPlayer(self):
        return self.currentPlayer

    def setWinner(self, winner):
        self.winner = winner
    
    def getPlayerCount(self):
        return numPlayers

    def playerTurn(self):
        return numPlayers - turn
    
    def getPlayer(self, turn):
        return players[turn]
    
    def createDeck(self):
        self.deck = Deck()
        self.deck.shuffle()

    def createPile(self):
        self.pile = Pile()
        self.deck.shuffle()
        setTopCard(self.pile.getFirstCard)
        setSecondCard(self.pile.getSecondCard)
        setThirdCard(self.pile.getThirdCard)
        return numPlayers

    def playerTurn(self):
        return numPlayers - turn

    def createDeck(self):
        self.deck = Deck()
        self.deck.shuffle()

    def createPile(self):
        self.pile = Pile()
        self.deck.shuffle()
        
    def runGame(self):
        theDeck = Deck(True)
        theDeck.shuffle()
        self.currentState.processCurrent()
        for p in self.players:
            p.setHand(Hand(theDeck, self.handSize))
        

"""Begin state machine for behavior of the game"""

class State:
    def __init__(self, Game)
        self.Game = Game;

    def setNextState(self, state):
        setCurrentState(state)

    def processCurrent(self):
        #custom to state
        return

    def slappable(firstCard, secondCard, thirdCard):
        if(firstCard.getRank() == secondCard.getRank()):
            return true
        elif(firstCard.getRank() == thirdCard.getRank()):
            return true
        else:
            return false
        """TODO(when there is more time): Bottoms up
                Tens
                Jokers
                4 in a Row
                Marriage"""

class Begin(State):

    def processCurrent(self):
        EgyptianRatsCrew.setCurrentPlayer()
        print("Player number" + turn + "is playing a Card\n")
        playingCard = EgyptianRatsCrew.getCurrentPlayer.playCard()
        getPile.addTopCard(playingCard) #adds a card to the pile
        print("The player has played a Card with the properties: Suit" + playingCard.getSuit() + " and Rank" + playingCard.getRank())

    def setNextState(self, state):
        setCurrentState(NonSlappable())
        

class Slappable(State):
    def processCurrent(self):
        setCurrentPlayer(players[turn])
        
    def setNextState(self, state):
        if(slappable(getTopCard(), getSecondCard(), getThirdCard())):
            setCurrentState(Slappable())
        else:
            setCurrentState(NonSlappable())

class NonSlappable(State):
    def processCurrent(self):
        setCurrentPlayer(players[turn])
        
    def setNextState(self, state):
        if(slappable(getTopCard(), getSecondCard(), getThirdCard())):
            setCurrentState(Slappable())
        else:
            setCurrentState(NonSlappable())

class End(State):
    
    def setWinningPlayer(self):
        setWinner(getCurrentPlayer())
    
    def processCurrent(self):
        setWinner()
    
    def setNextState(self):
        #nothing
        return
    
    #Testing
sample = EgyptianRatsCrew({"Billy", "Joe"})
sample.runGame()
