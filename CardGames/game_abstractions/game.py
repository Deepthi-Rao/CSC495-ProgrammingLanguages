from persistent.player import Player
from persistent.deck import Deck
from persistent.pile import Pile

"""This defines the game class """

class Game:

    #gameName will be the name of the game
    
    def __init__(self, gameName, players, inQueue, outQueue):
        self.name, self.currentTurn = gameName, 0
        self.msgsIn, self.msgsOut = inQueue, outQueue
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs'],
        self.ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
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

    def canonRank(self, rank):
        upperRank = rank.upper()
        if upperRank in self.ranks:
            return upperRank
        if upperRank == 'T':
            return '10'
        return None

    def canonSuit(self, suit):
        upperSuit = suit.upper()
        for s in self.suits:
            if upperSuit == s.upper() or upperSuit == s.upper()[0]:
                return s
        return None

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

    def getValue(self, card):
        if card.getRank() in self.ranks:
            return self.ranks.index(card.getRank())
        return 0

    def getTopCard(self):
        return self.treatedCard

    def nextRank(self, rank):
        if rank in self.ranks:
            rankIndex = self.ranks.index(rank)
            rankIndex += 1
            if rankIndex >= len(self.ranks):
                rankIndex -= self.ranks
            return self.ranks[rankIndex]
        return None

    def playCard(self, player, card, treatedCard):
        player.playCard(card)
        self.discard.placeOnTop(card)
        self.treatedCard = treatedCard

    def getCard(self, msg, startIndex):
        tokens = msg.upper().split()
        if len(tokens) < startIndex + 1:
            return (None, 0)
        if tokens[startIndex] == 'JOKER':
            return (Card('Joker', None), 1)
        if len(tokens) < startIndex + 3:
            return (None, 0)
        if not tokens[startIndex + 1] == 'OF' and not tokens[startIndex + 1] == 'O':
            return (None, 0)
        rank = tokens[startIndex]
        suit = tokens[startIndex + 2]
        rank = self.canonRank(rank)
        suit = self.canonSuit(suit)
        if not rank or not suit:
            return (None, 0)
        return (Card(rank, suit), 3)

    def extractCard(self, msg, player, startIndex):
        card, numTokens = self.getCard(msg, startIndex)
        if not card or card not in player.getCardsInHand():
            return (None, None, 0)
        subCard = card
        if card.isJoker():
            subCard, subTokens = self.getCard(msg, startIndex + numTokens)
            numTokens += subTokens
            if not subCard or subCard.isJoker():
                return (None, None, 0)
        return (card, subCard, numTokens)
