from utils.stack import Stack

class Pile(Stack):

    def __init__(self):
        self.stack = []
    
    def clearCardsFromPile(self): #returns cards until that point in time
        for card in self.cards:
            card.returnToDeck()
        self.cards = [] #clear card in the pile

    def placeOnTop(self, card):
        self.push(card)
    
