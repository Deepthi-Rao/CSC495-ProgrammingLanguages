from persistent.player import Player
from persistent.deck import Deck
from persistent.pile import Pile

"""This defines the game class """

class Game:

    #gameName will be the name of the game
    
    def __init__(self, gameName):
        self.name, self.currentTurn = gameName, 0
        self.pile = Pile()
        self.winner, self.currentPlayer = None
        

    def setPlayers(self, numPlayers, players):
        self.players = [Player(p) for p in players]
        self.numPlayers = numPlayers
    
    def selectDeck(self, jokers):
        self.deck = Deck(jokers)
    
    def drawCards(self, player, numCards):
        player.getHand().addCards(self.deck.deal(numCards))
   
    def setCurrentPlayer(self, currentPlayer):
        self.currentPlayer = currentPlayer

    def getCurrentPlayer(self):
        return self.currentPlayer

    def setWinner(self, winner):
        self.winner = winner

    def runGame(self):
        if self.name == "ERS" or self.name == "Egyptian Rat Screw":
            self.selectDeck(False)
        elif self.name == "TLO" or self.name == "The Last One":
            self.selectDeck(True)
        self.deck.shuffle()

    def getPlayerCount(self):
        return self.numPlayers
    
    def fetchMsgs(self):
        pass
