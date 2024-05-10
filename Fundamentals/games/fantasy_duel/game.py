from knight import Knight
from wizard import Wizard
from dragon import Dragon


def main():
    print("Choose your character:")
    print("1. Knight")
    print("2. Wizard")
    choice = input("Select your hero (1-2): ")

    if choice == '1':
        player = Knight("Sir Lancelot", 120)  # Increased health for balance
    elif choice == '2':
        player = Wizard("Merlin", 100)  # Increased health for balance

    dragon = Dragon("Smaug", 120)  # Decreased dragon's health for balance

    print(f"\n{player.name} faces off against {dragon.name}!")
    print(f"Starting health - {player.name}: {player.health}, {dragon.name}: {dragon.health}")

    while player.health > 0 and dragon.health > 0:
        print(f"\n{player.name} Health: {player.health}, {dragon.name} Health: {dragon.health}")
        print("What will you do?")
        print("1. Attack")
        print("2. Special Move")
        print("3. Flee")
        action = input("Choose an action (1-3): ")

        if action == '1':
            player.attack(dragon)
        elif action == '2':
            player.special_move(dragon)
        elif action == '3':
            print(f"{player.name} flees from the battle. Game over.")
            break

        if dragon.health <= 0:
            print(f"{dragon.name} has been defeated!")
            break

        # Implementing a cooldown for dragon's attack
        if dragon.health > 60 or player.health < 30:
            dragon.attack(player)
            if player.health <= 0:
                print(f"{player.name} has fallen in battle.")
                break
        else:
            print(f"{dragon.name} is gathering strength for the next attack.")

if __name__ == "__main__":
    main()
