class CardType:
    Clubs=0
    Diamonds=1
    Spades=2
    Hearts=3

class CardValue:
    A='1'
    J='11'
    Q='12'
    K='13'
    B_Joker='Big Joker'
    S_Jocker='Small Jocker'


class Card:
    def __init__(self, value, c_type):
        self.value = value
        self.c_type = c_type

    def __str__(self):
        # ♥♦♠♣
        mtype = ''
        if self.c_type == CardType.Hearts:
            mtype = '♥'
        elif self.c_type == CardType.Diamonds:
            mtype = '♦'
        elif self.c_type == CardType.Spades:
            mtype = '♠'
        elif self.c_type == CardType.Clubs:
            mtype = '♣'
        return mtype + self.value

    def is_same_type(self, card):
        if type(self) is type(card):
            if card is self.c_type:
                return True
            else:
                return False
        else:
            raise Exception('Error Class')
