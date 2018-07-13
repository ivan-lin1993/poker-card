from .card import Card
from .card import CardType
import random

class Deck:
    def __init__(self):
        self.deck = []
        self.size = 52
        for i in range(self.size):
            j = i % 4
            if j == 0:
                card_type = CardType.Clubs
            elif j == 1:
                card_type = CardType.Diamonds
            elif j == 2:
                card_type = CardType.Hearts
            elif j == 3:
                card_type = CardType.Spades
            card = Card( str((i%13)+1), card_type)
            self.deck.append(card)
    
    def __str__(self):
        res = ""
        for i in range(self.size):
            res += str(self.deck[i])+" "
        return res


    def shuffle(self):
        after_shuffle = []
        total = self.size -1
        for i in range(self.size):
            ind = random.randint(0, total)
            after_shuffle.append(self.deck.pop(ind))
            total -= 1
        self.deck = after_shuffle