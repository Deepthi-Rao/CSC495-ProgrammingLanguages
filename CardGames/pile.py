from stack import Stack
class Pile(Stack):

    def __init__(self, deck):
        self.deck = deck
        self.cards = []
    
    def clearCardsFromPile(self): #returns cards until that point in time
        for card in self.cards:
            card.returnToDeck()
        self.cards = [] #clear card in the pile


    
