from game_abstractions.game import Game
from persistent.hand import Hand

"""TODO:make a pile and move all some deck functions into pile
        make it so that each player plays their top card
        check if slappable or not
        check if deck has zero cards and each player has zero card game ends"""
#gameName will be the name of the game
#players will be a string of player IDs
class EgyptianRatScrew(Game):
    
    def __init__(self, playersID):
        super()
        self.name = "Egyptian Rat Screw"
        self.numPlayers = len(playersID)
        if(52 % self.numPlayers == 0):
            self.handSize = 52 / self.numPlayers

        #else: #handles over flow cards
            #redistribute()

        super.setPlayers(self.numPlayers, playersID)
        
        self.currentPlayer = self.players[0] #first entered is the first player
        self.setCondition()
        self.currentState = Begin(self)
        self.msgs = []

    def getPile(self):
        return self.pile

    def setCurrentPlayer(self):
        self.currentPlayer = self.players[self.turn % self.numPlayers]

    def setCurrentState(self, state):
        self.currentState = state;

    def getCurrentState(self):
        return self.currentState

    def getCurrentPlayer(self):
        return self.currentPlayer

    def getPlayerCount(self):
        return
    
    def getCurrentTurn(self):
        return self.turn % self.numPlayers
    
    def setCurrentTurn(self, turn):
        self.turn = turn

    def setWinner(self, winner):
        self.winner = winner

    def getPlayer(self, turn):
        assert isinstance(turn, int)
        return self.players[turn]
        
    def setCondition(self):
        for p in self.players:
            p.setHand(Hand(self.deck, self.handSize))

    def play(self):
        return self.currentState.processCurrent(self)
        
    def appendMsg(self, msg):
        self.msgs.append(([p.getId() for p in self.players], msg))

    def fetchMsgs(self):
        tmp = self.msgs
        self.msgs = []
        return tmp

"""Begin state machine for behavior of the game"""

class State:
    def __init__(self, Game):
        self.Game = Game;

    def setNextState(self, state, Game):
        return

    def processCurrent(self, Game):
        #custom to state
        return

    def slappable(self, firstCard, secondCard): #most of game logic will be here regarding slaps
        if(firstCard.getRank() == secondCard.getRank()):
            return True
        #elif(firstCard.getRank() == thirdCard.getRank()):
            #return True
        else:
            return False
        """TODO(when there is more time): Bottoms up
                Tens
                Jokers
                4 in a Row
                Marriage"""

class Begin(State):

    def processCurrent(self, Game):
        Game.setCurrentPlayer()
        Game.appendMsg(Game.getCurrentPlayer().getId() + " is playing a Card")
        playingCard = Game.getCurrentPlayer().playTopCard()
        Game.getPile().addCardToTop(playingCard) #adds a card to the pile
        Game.appendMsg(Game.getCurrentPlayer().getId() + " has played a Card with the properties: Suit " + playingCard.getSuit() + " and Rank "
              + str(playingCard.getRank()))
        return self.setNextState(Game)

    def setNextState(self, Game):
        Game.setCurrentState(NonSlappable(Game))
        Game.setCurrentTurn(Game.getCurrentTurn() + 1)
        Game.appendMsg("Not Slappable")
        return Game.fetchMsgs()

class Slappable(State):
    def processCurrent(self, Game):
        Game.setCurrentPlayer()
        Game.appendMsg(Game.getCurrentPlayer().getId() + " is playing a Card")
        playingCard = Game.getCurrentPlayer().playTopCard()
        Game.getPile().addCardToTop(playingCard)  # adds a card to the pile
        Game.appendMsg(Game.getCurrentPlayer().getId() + " has played a Card with the properties: Suit " + playingCard.getSuit() + " and Rank "
              + str(playingCard.getRank()))
        return self.setNextState(Game)
        
    def setNextState(self, Game):
        if(self.slappable(Game.getTopCard(), Game.getSecondCard())):
            Game.setCurrentState(Slappable(Game))
            Game.setCurrentTurn(Game.getCurrentTurn() + 1)
            Game.appendMsg("Slappable")
            return Game.fetchMsgs()
        else:
            Game.setCurrentState(NonSlappable(Game))
            Game.setCurrentTurn(Game.getCurrentTurn() + 1)
            Game.appendMsg("Not Slappable")
            return Game.fetchMsgs()

class NonSlappable(State):
    def processCurrent(self, Game):
        Game.setCurrentPlayer()
        Game.appendMsg(Game.getCurrentPlayer().getId() + " is playing a Card")
        playingCard = Game.getCurrentPlayer().playTopCard()
        Game.getPile().addCardToTop(playingCard)  # adds a card to the pile
        Game.appendMsg(Game.getCurrentPlayer().getId() + " has played a Card with the properties: Suit " + playingCard.getSuit() + " and Rank "
              + str(playingCard.getRank()))
        return self.setNextState(Game)
        
    def setNextState(self, Game):
        if(self.slappable(Game.getTopCard(), Game.getSecondCard())):
            Game.setCurrentState(Slappable(Game))
            Game.setCurrentTurn(Game.getCurrentTurn() + 1)
            Game.appendMsg("Slappable")
            return Game.fetchMsgs()
        else:
            Game.setCurrentState(NonSlappable(Game))
            Game.setCurrentTurn(Game.getCurrentTurn() + 1)
            Game.appendMsg("Not Slappable")
            return Game.fetchMsgs()

class End(State):
    
    def setWinningPlayer(self, Game):
        Game.setWinner(Game.getCurrentPlayer())
    
    def processCurrent(self, Game):
        Game.setWinner()
    
    def setNextState(self):
        #nothing
        return
    
#Interaction
if __name__ == '__main__':
    print("____Welcome to Egyptian Rat Screw____")
    print("")
    print("")
    players = list()
    numPlayers = input("How many players would you like? (Please enter even number of players only) : ")
    print("")
    print("")
    print("You will now be prompted for player ID, enter the IDs in the you would like the player to play")
    for i in range(0, numPlayers):
        player = input("What is the name of player " + str(i) + " ? ")
        players.append(str(player))
    print("")
    print("")
    print("Game is being constructed with parameters given:")
    print("Number of Players " + str(numPlayers))
    print("Player IDs " + str(players))
    print("")
    print("")
    currentGame = EgyptianRatScrew(players)
    print("Game Has Started")
    print("")
    print("")
    print("Enter 'play' to place a card on the stack, if anything is entered game will exit")
    print("")
    print("")
    command = input("Enter a command: ")
    while command == "play":
        currentGame.play()
        command = input("Enter a command: ")
    print("")
    print("")
    print("exiting program")
