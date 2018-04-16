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
        self.machines = []

    def addMachine(self, machine):
        self.machines.append(machine)

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
                for machine in self.machines:
                    machine.processMsg(msg, player)

    def getPlayerCount(self):
        return self.numPlayers

    def getPlayer(self, playername):
        for p in self.players:
            if p.getName() == playername:
                return p
    
    def fetchMsgs(self):
        pass
