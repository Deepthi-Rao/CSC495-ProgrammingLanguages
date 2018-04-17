from game_abstractions.game import Game
from game_abstractions.rule import Rule
#This class defines the rules for the last one
class TheLastOneRules:

    #initializes the class of all the Rules for the last one
    def __init__(self, Game):
        self.game = Game
        self.game.addRule(self.queryHand)
        self.game.addRule(self.queryOthersCardNums)
        self.game.addRule(self.play)
        self.game.addPlayRule(self.twoRule)
        self.game.addPlayRule(self.threeRule)
        self.game.addPlayRule(self.fourRule)
        self.game.addPlayRule(self.eightRule)
        self.game.addPlayRule(self.jackRule)
        self.game.addPlayRule(self.aceRule)
        self.game.addPlayRule(self.playRule)

    #this is the rule to pay a card
    def playRule(Rule):
        def __init__(self, msg, player, card, subCard, numTokens, Game):
            super().__init__(msg, player, card, subCard, numTokens, Game)

            if self.game.canPlay(subCard):
                self.game.playCard(player, card, subCard)
                self.game.nextPlayer()

    #defines rules is card rank rank is two
    def twoRule(Rule):
        def __init__(self, msg, player, card, subCard, numTokens, Game):
            super().__init__(msg, player, card, subCard, numTokens, Game)

            if self.game.cardIs(subCard, rank='2') and self.game.canPlay(subCard):
                self.game.playCard(player, card, subCard)
                self.game.nextPlayer()
                self.game.drawCards(self.getCurrentPlayer(), 2)
                self.game.nextPlayer()

    # defines rules is card rank rank is three
    def threeRule(Rule):
        def __init__(self, msg, player, card, subCard, numTokens, Game):
            super().__init__(msg, player, card, subCard, numTokens, Game)

            if self.game.cardIs(subCard, rank='3') and self.game.canPlay(subCard):
                self.game.playCard(player, card, subCard)
                self.game.canPlayAny = True

    # defines rules is card rank rank is Four
    def fourRule(Rule):
        def __init__(self, msg, player, card, subCard, numTokens, Game):
            super().__init__(msg, player, card, subCard, numTokens, Game)
            if self.game.cardIs(subCard, rank='4') and self.game.canPlay(subCard):
                self.game.playCard(player, card, subCard)
                self.game.startMelee()

    # defines rules is card rank rank is eight
    def eightRule(self, msg, player, card, subCard, numTokens):
        if self.cardIs(subCard, rank='8'):
            suit, usedTokens = self.extractSuit(msg, numTokens + 1)
            if not suit:
                self.sendMessage(self.thisPlayer(player), 'Invalid Suit')
                return
            self.playCard(player, card, subCard)
            self.setSuit(suit)
            self.nextPlayer()

    # defines rules is card rank rank is a jack
    def jackRule(Rule):
        def __init__(self, msg, player, card, subCard, numTokens, Game):
            super().__init__(msg, player, card, subCard, numTokens, Game)
            if self.game.cardIs(subCard, rank='J') and self.game.canPlay(subCard):
                self.game.playCard(player, card, subCard)
                self.game.nextPlayer()
                self.game.nextPlayer()

    # defines rules is card rank rank is an ace
    def aceRule(Rule):
        def __init__(self, msg, player, card, subCard, numTokens, Game):
            super().__init__(msg, player, card, subCard, numTokens, Game)
            if self.game.cardIs(subCard, rank='A') and self.game.canPlay(subCard):
                self.game.playCard(player, card, subCard)
                self.game.reversePlay()
                self.game.nextPlayer()

    # defines behavior if card is queried
    def queryHand(Rule):
        def __init__(self, msg, Player):
            super().__init__(self, msg, Player)
            if msg.upper() == 'HAND':
                self.sendMessage(self.thisPlayer(self.player), self.player.viewHand())

    #defines behavio if card num is queried
    def queryOthersCardNums(Rule):
        def __init__(self, msg, Player):
            super().__init__(self, msg, Player)
            if msg.upper() == 'OTHERS':
                self.sendMessage(self.thisPlayer(self.player), self.othersHands(self.player))

    #defines the behavior if a card is played
    def play(Rule):
        def __init__(self, msg, Player):
            super().__init__(self, msg, Player)
            if self.isMelee:
                self.meleeRule(msg, player)
            else:
                self.handlePlayRules(msg, player)


