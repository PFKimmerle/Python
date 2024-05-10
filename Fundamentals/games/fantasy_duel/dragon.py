from character import Character

class Dragon(Character):
    def attack(self, other):
        damage = 25  # Fire breath attack
        other.health -= damage
        print(f"{self.name} breathes fire on {other.name} for {damage} damage.")