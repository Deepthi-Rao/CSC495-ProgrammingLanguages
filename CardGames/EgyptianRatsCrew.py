from Game import Game, State
from Player import Player
from Deck import Card, Deck
from Hand import Hand
"""TODO:make a pile and move all some deck functions into pile
        make it so that each player plays their top card
        check if slappable or not
        check if deck has zero cards and each player has zero card game ends"""
class EgyptianRatsCrew(Game):
    
    def __init__(self, players, numPlayers):
        self.name = "Egyptian Rats Crew"

        if(52 % numPlayers == 0):
            self.handSize = handSize

        else: #handles over flow cards
            redistribute()

        self.players = [Player(p) for p in players]

        self.currentPlayer = players[0] #first entered is the first player
        self.currentState = Begin()
        self.numPlayers = numPlayers
        self.turn = numPlayers - 1
        self.pile = []

    def runGame(self):
        theDeck = Deck(True)
        theDeck.shuffle()
        for p in self.players:
            p.setHand(Hand(theDeck, self.handSize))


class State:

    def __init__(self, stateName):
        self.stateName = stateName

    def setNextState( self, state):
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
        setCurrentPlayer(players[turn])

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
    