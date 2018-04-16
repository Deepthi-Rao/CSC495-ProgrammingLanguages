class Card:
    def __repr__(self):
        if self.rank == None or self.suit == None:
            return "Joker"
        return self.rank + " of " + self.suit
        
    def __str__(self):
        if self.rank == None or self.suit == None:
            return "Joker"
        return self.rank + " of " + self.suit
        
    def __init__(self, rank, suit):
        self.rank, self.suit, self.isDealt = rank, suit, False
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.rank == other.rank and self.suit == other.suit
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def getSuit(self):
        return self.suit

    def setSuit(self, suit):
        self.suit = suit
        
    def getRank(self):
        return self.rank
        
    def isJoker(self):
        if self.rank == "Joker":
            return True
        return False
    
    def isDealt(self):
        return self.isDealt
        
    def dealMe(self):
        self.isDealt = True
        
    def returnToDeck(self):
        self.isDealt = False
    
    def match(self, other):
        if self.isJoker() and other.isJoker():
            return True
        elif str(self.rank) == str(other.rank) and self.suit == other.suit:
            return True
        return False
