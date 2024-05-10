from character import Character

class Wizard(Character):
    def attack(self, other):
        damage = 15
        other.health -= damage
        print(f"{self.name} casts a minor spell on {other.name} for {damage} damage.")

    def special_move(self, other):
        damage = 30
        # Adds a chance for a critical hit
        critical = damage * 2 if self.health < 30 else damage
        other.health -= critical
        action = "unleashes a devastating spell" if critical > damage else "casts a powerful spell"
        print(f"{self.name} {action} on {other.name} for {critical} damage.")