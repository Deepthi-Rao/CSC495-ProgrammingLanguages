class Card:
    def __repr__(self):
        if self.rank == None or self.suit == None:
            return "Joker"
        return str(self.rank) + " of " + self.suit
        
    def __str__(self):
        if self.rank == None or self.suit == None:
            return "Joker"
        return str(self.rank) + " of " + self.suit
        
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.isDealt = False
    
    def getSuit(self):
        return self.suit
        
    def getRank(self):
        return self.rank
        
    def isJoker(self):
        if self.rank == "joker":
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