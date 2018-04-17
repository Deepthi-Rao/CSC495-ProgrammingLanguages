from game_abstractions.game import Game
from game_abstractions.rules import *
from persistent.player import Player
from persistent.deck import Deck
from persistent.card import Card
from persistent.hand import Hand
from persistent.pile import Pile
from game_abstractions.rule import Rule

class TheLastOne(Game):
    def __init__(self, players, inQueue, outQueue):
        super().__init__("The Last One", players, inQueue, outQueue, jokers=True, timeLastCard=True)
        self.playRules = []
        self.aggressor, self.aggressee, self.isMelee, self.canPlayAny = None, None, False, False
        self.unpassPlayers()
        self.setWinCondition(self.winLastOne)
        self.deal(6)
        self.playFirstCard()
        for p in self.players:
            self.sendMessage(self.thisPlayer(p), p.viewHand())
        self.sendMessage(self.allPlayers(), 'The top card is: ' + str(self.getTopCard()))

    def deal(self, handSize):
        for p in self.players:
            p.setHand(Hand())
        for _ in range(handSize):
            for p in self.players:
                p.getHand().addCard(self.deck.draw())

    def playFirstCard(self):
        firstCard = Card('Joker', None)
        while firstCard.isJoker():
            firstCard = self.deck.draw()
            self.discard.placeOnTop(firstCard)
            self.treatedCard = firstCard

    def winLastOne(self, player):
        return player.hasNoCards()

    def callLast(self, msg, player):
        if self.lastCardTime and msg.upper() == 'LAST ONE':
            self.unsetTimer(player)

    def callFail(self, msg, player):
        if self.lastCardTime and msg.upper() == 'FAILED TO CALL':
            failure, failedPlayer = self.failTimer(5, 5)
            if failure:
                self.drawCards(failedPlayer, 1)

    def canPlay(self, card):
        return self.canPlayAny or cardRankOrSuitIs(card, rank=self.getTopCard().getRank(), suit=self.getTopCard().getSuit())

    def unpassPlayers(self):
        self.passPlayers = []

    def passPlayer(self, player):
        if player not in self.passPlayers:
            self.passPlayers.append(player)

    def meleeRule(self, msg, player):
        if firstWord(msg).upper() == 'PLAY' and not player == self.aggressor:
            card, subCard, numTokens = self.extractCard(msg, player, 1)
            if not numTokens:
                self.sendMessage(self.thisPlayer(player), 'Invalid Card')
                return
            topCard = self.getTopCard()
            if not cardIs(subCard, rank=self.nextRank(topCard.getRank()), suit=topCard.getSuit()):
                self.sendMessage(self.thisPlayer(player), 'Invalid Card')
                return
            self.playCard(player, card, subCard)
            self.aggressee = self.aggressor
            self.aggressor = player
            self.unpassPlayers()
            self.sendMessage(self.allPlayers(), 'Aggressor is: ' + self.aggressor.getName())
            self.sendMessage(self.allPlayers(), 'Aggressee is: ' + self.aggressee.getName())
        elif msg.upper() == 'PASS':
            self.passPlayer(player)
            for p in self.players:
                if not p == self.aggressor and p not in self.passPlayers:
                    return
            self.sendMessage(self.allPlayers(), 'Melee has ended.')
            self.drawCards(self.aggressee, self.getValue(self.getTopCard()))
            self.isMelee = False
            self.unpassPlayers()
            self.nextPlayer()

    def startMelee(self):
        self.isMelee = True
        self.aggressor = self.getCurrentPlayer()
        self.aggressee = self.sampleNextPlayer()
        self.sendMessage(self.allPlayers(), 'Melee has started.')
        self.sendMessage(self.allPlayers(), 'Aggressor is: ' + self.aggressor.getName())
        self.sendMessage(self.allPlayers(), 'Aggressee is: ' + self.aggressee.getName())


    def handlePlayRules(self, msg, player):
        if player == self.getCurrentPlayer():
            if firstWord(msg) == 'PLAY':
                card, subCard, numTokens = self.extractCard(msg, player, 1)
                if not numTokens:
                    self.sendMessage(self.thisPlayer(player), 'Invalid Card')
                    return

                for r in self.playRules:
                    Rule(msg, player, card, subCard, numTokens,self)
            elif msg.upper() == 'DRAW':
                self.drawCards(player, 1)

    def addPlayRule(self, rule):
        self.playRules.append(rule)
