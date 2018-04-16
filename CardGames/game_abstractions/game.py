from persistent.player import Player
from persistent.deck import Deck
from persistent.pile import Pile

"""This defines the game class """

class Game:

    #gameName will be the name of the game
    
    def __init__(self, gameName, players, inQueue, outQueue):
        self.name, self.currentTurn = gameName, 0
        self.msgsIn, self.msgsOut = inQueue, outQueue
        self.pile = Pile()
        self.setPlayers(players)
        self.winner, self.currentPlayer = None, None
        self.rules, self.slapConditions = [], []

    def addRule(self, rule):
        self.rules.append(rule)

    def setPlayers(self, players):
        self.players = [Player(p) for p in players]
        self.numPlayers = len(players)
    
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

    def run(self):
        while not self.winner:
            self.msgsIn.waitForEvent()
            while self.msgsIn.notEmpty():
                inMsg = self.msgsIn.dequeue()
                player = self.getPlayer(inMsg[0])
                msg = inMsg[1]
                for rule in self.rules:
                    rule(msg, player)

    def getPlayerCount(self):
        return self.numPlayers

    def getPlayer(self, playername):
        for p in self.players:
            if p.getName() == playername:
                return p
    
    def thisPlayer(self, player):
        return [player.getName()]

    def otherPlayers(self, player):
        return [p.getName() for p in self.players if not p == player]

    def allPlayers(self):
        return [p.getName() for p in self.players]

    def sendMessage(self, recipients, msg):
        self.msgsOut.enqueue((recipients, msg))

    def isSlappable(self):
        for condition in self.slapConditions:
            if condition():
                return True
        return False

    def othersHands(self, player):
        return ', '.join([p.getName() + ': ' + str(p.numCards()) for p in self.players if not p == player])

    def addSlapCondition(self, condition):
        self.slapConditions.append(condition)
