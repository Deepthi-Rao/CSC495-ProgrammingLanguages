class Rules:
    
    def __init__(self):
        pass

def cardIs(card, *, rank=None, suit=None):
    if not rank and not suit:
        raise Exception("Invalid isCard use. Must define rank or suit.")
    if rank and not card.getRank() == rank:
        return False
    if suit and not card.getSuit() == suit:
        return False
    return True

def firstWord(msg):
    return msg.split()[0]

