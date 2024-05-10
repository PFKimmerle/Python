class Companion:
    def __init__(self, name, species, skills):
        self.name = name
        self.species = species
        self.skills = skills
        self.health = 100
        self.energy = 50

    def rest(self):
        self.energy += 25
        print(f"{self.name} is resting. Energy increased to {self.energy}.")

    def snack(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is snacking. Health increased to {self.health}, Energy increased to {self.energy}.")

    def adventure(self):
        self.health += 5
        print(f"{self.name} is adventuring. Health increased to {self.health}.")

    def sound(self):
        print(f"{self.name} makes an excited sound!")
