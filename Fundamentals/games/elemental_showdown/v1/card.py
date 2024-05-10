class Card:
    def __init__(self, element, power):
        self.element = element
        self.power = power

    def __repr__(self):
        return f"{self.element} Card with Power {self.power}"
