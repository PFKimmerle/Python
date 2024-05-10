from deck import Deck

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.hand = []

    def draw_card(self, deck):
        card = deck.draw()
        if card:
            self.hand.append(card)

    def play_card(self, index):
        if 0 <= index < len(self.hand):
            return self.hand[index]  # Keep the card in the hand after playing
        return None

    def show_hand(self):
        for idx, card in enumerate(self.hand):
            print(f"{idx}: {card}")
