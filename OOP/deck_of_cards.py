from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
    value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Deck.suit for value in Deck.value]

    def __repr__(self):
        return f"Deck of {self.count()} cards"
    
    def count(self):
        return len(self.cards)
    
    def _deal(self, num):
        count = self.count()
        if count == 0:
            raise ValueError("All cards have been dealt")
        actual = min([count, num])
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self
    
    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self, size):
       return self._deal(size)
