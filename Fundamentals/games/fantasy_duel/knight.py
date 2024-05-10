from character import Character

class Knight(Character):
    def attack(self, other):
        damage = 20
        other.health -= damage
        print(f"{self.name} strikes {other.name} with a sword for {damage} damage.")

    def special_move(self, other):
        if self.health < 50:
            heal = 30
            self.health += heal
            print(f"{self.name} uses Rally Cry to heal himself for {heal} health.")
        else:
            damage = 35
            other.health -= damage
            print(f"{self.name} performs a heroic charge on {other.name}, dealing {damage} damage.")