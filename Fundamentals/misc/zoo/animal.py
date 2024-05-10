class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.happiness = 100

    def display_info(self):
        print(f"{self.name} - Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10

class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health = 150
        self.happiness = 150

    def roar(self):
        print(f"{self.name} roars loudly!")

class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health = 120
        self.happiness = 120

    def feed(self):
        super().feed()
        self.happiness += 5  # Tigers get a little extra happiness when fed

class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health = 200
        self.happiness = 80  # Bears start a bit grumpier

    def feed(self):
        super().feed()
        self.health += 5  # Bears gain extra health when fed

    def sleep(self):
        print(f"{self.name} is hibernating. Zzz...")
