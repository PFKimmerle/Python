import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(element, power) for element in ['Water', 'Fire', 'Earth', 'Air'] for power in range(1, 11)]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None
