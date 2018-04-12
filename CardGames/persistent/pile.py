from utils.stack import Stack
from persistent_abstractions.faceup import FaceUp

class Pile(Stack, FaceUp):

    def __init__(self):
        self.stack = []
    
    def clearCardsFromPile(self): #returns cards until that point in time
        for card in self.cards:
            card.returnToDeck()
        self.cards = [] #clear card in the pile


    
