from companion import Companion

class Adventurer:
    def __init__(self, first_name, last_name, snacks, food, companion):
        self.first_name = first_name
        self.last_name = last_name
        self.snacks = snacks
        self.food = food
        self.companion = companion

    def go_on_adventure(self):
        print(f"{self.first_name} is adventuring with {self.companion.name}.")
        self.companion.adventure()

    def feed_companion(self):
        print(f"{self.first_name} is feeding {self.companion.name}.")
        self.companion.snack()

    def bathe_companion(self):
        print(f"{self.first_name} is bathing {self.companion.name}.")
        self.companion.sound()
