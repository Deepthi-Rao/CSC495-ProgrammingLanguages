from persistent.card import Card
from utils.stack import Stack

class Deck(Stack):
    def __repr__(self):
        return self.__class__.__name__
        
    def __init__(self, suits, ranks, jokers=False):
        print('suits: ' + str(suits))
        print('ranks: ' + str(ranks))
        self.stack = [Card(rank, suit) for rank in ranks for suit in suits]
        if jokers:
            self.stack.append(Card("Joker", None))
            self.stack.append(Card("Joker", None))
        
    def __len__(self):
        return self.size
  
    def deal(self, numCards):
        return [self.pop() for _ in range(numCards)]

    def draw(self):
        return self.pop()
