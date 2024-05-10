class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, other):
        raise NotImplementedError("Subclasses must implement this method.")