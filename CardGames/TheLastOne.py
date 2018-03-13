from Game import Game
from Player import Player
from Deck import Card, Deck
from Hand import Hand
from Pile import Pile

class State():
    def __repr__(self):
        return self.__class__.__name__
    
    def __eq__(self, other):
        return self.__repr__() == other.__repr__()
        
class BeginState(State):
    def __repr__(self):
        return self.__class__.__name__
        
class TurnState(State):
    def __repr__(self):
        return self.__class__.__name__ 
        
    def __init__(self):
        self.player = None
    
    def setPlayer(self, player):
        self.player = player
        
    def processMessage(self, game, player, msg):
        if msg.lower() == "draw":
            game.setState(TurnState())
            print("Drawing one card.")
            player.viewHand()
            player.hand.addCards(list(game.theDeck.deal(1)))
            return
        
        cardToPlay = game.pickCard(player, msg)
        activeCard = game.pile.getFirstCard()
        
        if cardToPlay is not None:
            if cardToPlay.getRank() == "joker":
                game.setState(JokerState())
                game.currentState.display()
                cardString = input("Define your card: ")
                cardPieces = cardString.split()
                cardToPlay = Card(cardPieces[0], cardPieces[-1])
            if (activeCard is None) or cardToPlay.getRank() == "joker" or (cardToPlay.getRank() == activeCard.getRank()) or (cardToPlay.getSuit() == activeCard.getSuit()):
                game.pile.addCardToTop(cardToPlay)
                player.hand.discard(cardToPlay)
                rank = str(cardToPlay.getRank())
                if rank == "2":
                    game.setState(TwoState())
                    game.currentState.display()
                elif rank == "3":
                    game.setState(ThreeState())
                    game.currentState.display()
                elif rank == "4":
                    game.setState(FourState(4, cardToPlay.getRank()))
                    game.currentState.display()
                elif rank == "8":
                    suit = input("Select your suit: ")
                    game.setState(EightState(suit))
                    game.currentState.display()
                elif rank == "J":
                    game.setState(JackState())
                    game.currentState.display()
                elif rank == "A":
                    game.setState(AceState(game))
                    game.currentState.display()
                else:
                    game.setState(TurnState())
                    
            else:
                print("Invalid card. Draw One.")
                player.hand.addCards(list(game.theDeck.deal(1)))
                player.viewHand()
                game.setState(TurnState())
        else:
            print("Invalid card: Not in hand. Draw One.")
            player.hand.addCards(list(game.theDeck.deal(1)))
            player.viewHand()
            game.setState(TurnState())
            
            
class TwoState(TurnState):
    def display(self):
        print("The next player must draw two cards from the stock, and is not allowed to play a card.")
        
    
class ThreeState(TurnState):
    def display(self):
        print("The current player may play any card on top of this card.")
        
    def processMessage(self, game, player, msg):
        cardToPlay = game.pickCard(player, msg)
        if cardToPlay is not None:
            if cardToPlay.getRank() == "joker":
                game.setState(JokerState())
                game.currentState.display()
                cardString = input("Define your card: ")
                cardPieces = cardString.split()
                cardToPlay = Card(cardPieces[0], cardPieces[-1])
            game.pile.addCardToTop(cardToPlay)
            player.hand.discard(cardToPlay)
            rank = str(cardToPlay.getRank())
            if rank == "2":
                game.setState(TwoState())
                game.currentState.display()
            elif rank == "3":
                game.setState(ThreeState())
                game.currentState.display()
            elif rank == "4":
                game.setState(FourState(4, cardToPlay.getRank()))
                game.currentState.display()
            elif rank == "8":
                suit = input("Select your suit: ")
                game.setState(EightState(suit))
                game.currentState.display()
            elif rank == "J":
                game.setState(JackState())
                game.currentState.display()
            elif rank == "A":
                game.setState(AceState())
                game.currentState.display()
            elif rank == "joker":
                game.setState(JokerState())
                game.currentState.display()
                cardString = input("Define your card: ")
                cardPieces = cardString.split()
                card = Card(cardPieces[0], cardPieces[-1])
                game.pile.addCardToTop(card)
            else:
                game.setState(TurnState())
        
        else:
            print("Invalid card: Not in hand. Draw one.")
            player.hand.addCards(list(game.theDeck.deal(1)))
            player.viewHand()
            game.setState(TurnState())
    
class FourState(TurnState):
    def __init__(self, currentRank, currentSuit):
        self.currentRank = currentRank
        self.currentSuit = currentSuit
        
    def display(self):
        print("Melee. If the next player (or any other player) has the next rank card of the same suit, they may play it. If no one plays the next card, the next player must draw from stock the number of cards equal to the value of the current card.")
    
    def processMessage(self, game, player, msg):
        cardToPlay = game.pickCard(player, msg)
        if cardToPlay is not None:
            if cardToPlay.getRank() == "joker":
                game.setState(JokerState())
                game.currentState.display()
                cardString = input("Define your card: ")
                cardPieces = cardString.split()
                cardToPlay = Card(cardPieces[0], cardPieces[-1])
            rank = cardToPlay.getRank()
            continueMeleeRank = self.currentRank + 1
            if continueMeleeRank == rank and self.currentSuit == cardToPlay.getSuit():
                game.pile.addCardToTop(cardToPlay)
                game.setState(FourState(continueMeleeRank))
                print("Melee continues.")
                return
            player.hand.addCards(list(game.theDeck.deal(self.currentRank)))
            print("Melee ends.")
            print("Card not played.")
            player.viewHand()
            game.setState(TurnState())
        else:
            player.hand.addCards(list(game.theDeck.deal(self.currentRank)))
            print("Melee ends.")
            print("No card played.")
            player.viewHand()
            game.setState(TurnState())
    
class EightState(TurnState):
    def __init__(self, suit):
        self.suit = suit
        
    def display(self):
        print("The current player announces a suit, and the next play should be in the announced suit.")
    
    def processMessage(self, game, player, msg):
        cardToPlay = game.pickCard(player, msg)
        if cardToPlay is not None:
            if cardToPlay.getRank() == "joker":
                game.setState(JokerState())
                game.currentState.display()
                cardString = input("Define your card: ")
                cardPieces = cardString.split()
                cardToPlay = Card(cardPieces[0], cardPieces[-1])
            if cardToPlay.getSuit() == self.suit:
                game.pile.addCardToTop(cardToPlay)
                player.hand.discard(cardToPlay)
                rank = str(cardToPlay.getRank())
                if rank == "2":
                    game.setState(TwoState())
                    game.currentState.display()
                elif rank == "3":
                    game.setState(ThreeState())
                    game.currentState.display()
                elif rank == "4":
                    game.setState(FourState(4, cardToPlay.getRank()))
                    game.currentState.display()
                elif rank == "8":
                    suit = input("Select your suit: ")
                    game.setState(EightState(suit))
                    game.currentState.display()
                elif rank == "J":
                    game.setState(JackState())
                    game.currentState.display()
                elif rank == "A":
                    game.setState(AceState())
                    game.currentState.display()
                elif rank == "joker":
                    game.setState(JokerState())
                    game.currentState.display()
                else:
                    game.setState(TurnState())
                    
            else:
                print("Invalid card. Draw one.")
                player.hand.addCards(list(game.theDeck.deal(1)))
                player.viewHand()
                game.setState(TurnState())
        else:
            print("Invalid card: Not in hand. Draw one.")
            player.hand.addCard(list(game.theDeck.deal(1)))
            player.viewHand()
            game.setState(TurnState())
    
    
class JackState(TurnState):
    def display(self):
        print("The next player skips a turn.")
    
class AceState(TurnState):
    def __init__(self, game):
        game.turns.reverse()
    
    def display(self):
        print("The direction of play is now reversed.")
    
class JokerState(TurnState):
    def display(self):
        print("The Joker can represent any card of the pack, at the choice of the current player.")
    
class WinState(State):
    def __repr__(self):
        return self.__class__.__name__
    
class TheLastOne(Game):
    BEGIN = BeginState()
    def __init__(self, handSize=6):
        self.name = "The Last One"
        self.theDeck = Deck(True)
        self.theDeck.shuffle()
        numPlayers = int(input("How many players?\n"))
        players = []
        for i in range(numPlayers):
            print("Player", i, "Enter your ID: ")
            playerID = input()
            players.append(Player(playerID))
        
        self.handSize = handSize
        self.players = players
        self.currentPlayer = None
        global BEGIN
        BEGIN = BeginState()
        self.currentState = BEGIN
        self.numTurns = len(players)
        self.turns = []
        self.pile = Pile()
        self.winner = None
        
    def runGame(self, handSize=6):
        TURN = TurnState()
        WIN = WinState() 
        TWO = TwoState()
        JACK = JackState()
        
        if handSize < 4 or handSize > 8:
            print("Invalid hand size. Using default setting.")
        else:
            self.handSize = handSize
        
        for p in self.players:
            cards = list(self.theDeck.deal(self.handSize))
            hand = Hand(cards, self.handSize)
            p.setHand(hand)
            turn = TurnState()
            turn.setPlayer(p)
            print(p)
            self.turns.append(turn)
        
        self.currentState = TURN
        
        while self.currentState != WIN:
            for turn in self.turns:
                self.currentPlayer = turn.player
                print("Current Player: ", turn.player)
                print("Active Card: ", self.pile.getFirstCard())
                turn.player.viewHand()
                if self.getCurrentState() != TWO and self.getCurrentState() != JACK:
                    msg = input("Play a card or Draw: ")
                    self.getCurrentState().processMessage(self, turn.player, msg)
                    if turn.player.hand.getNumCardsInHand() == 0:
                        self.currentState = WIN
                        self.winner = self.currentPlayer
                        break
                elif self.getCurrentState() == TWO:
                    turn.player.hand.addCards(list(self.theDeck.deal(2)))
                    turn.player.viewHand()
                    self.currentState = TurnState()   
                elif self.getCurrentState() == JACK:
                    turn.player.viewHand()
                    self.currentState = TurnState() 
            
        
        print(self.currentPlayer, " IS THE WINNER")
        
        
    def pickCard(self, player, cardString):
        cards = player.hand.getCardsInHand()
        if cardString.lower() == "joker":
            joker = Card("joker", None)
            for card in cards:
                if card.match(joker):
                    return card
        else:
            splitString = cardString.split()
            rank = splitString[0]
            suit = splitString[-1]
            myCard = Card(rank, suit)
            for card in cards:
                if card.match(myCard):
                    return card
            
            return None
            
    def setState(self, state):
        self.currentState = state

        

if __name__ == '__main__':
    game = TheLastOne()
    game.runGame(4)

