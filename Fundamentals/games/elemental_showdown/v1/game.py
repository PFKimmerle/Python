from player import Player
from deck import Deck

def introduction():
    print("Welcome to Elemental Showdown!")
    print("In a world torn by elemental forces, two beings emerge as leaders of their factions.")
    print("One, a Hero seeking to bring peace. The other, a Villain, driven by the chaos of power.")
    print("Choose your side and battle using the elemental cards to either save or dominate the world.\n")

def apply_damage(player, opponent, player_card, opponent_card):
    player_damage = player_card.power  # Simple damage application
    opponent_damage = opponent_card.power
    
    opponent.health -= player_damage
    player.health -= opponent_damage

    print(f"{player.name} deals {player_damage} damage to {opponent.name}.")
    print(f"{opponent.name} deals {opponent_damage} damage to {player.name}.")

def main():
    introduction()
    deck = Deck()
    deck.shuffle()

    print("Choose your character:")
    print("1. Hero")
    print("2. Villain")
    choice = input("Select your character (1-2): ")

    if choice == '1':
        player = Player("Hero", 50)
        opponent = Player("Villain", 50)
    else:
        player = Player("Villain", 50)
        opponent = Player("Hero", 50)
    
    print(f"\n{player.name} faces off against {opponent.name}!")
    print("Both start with 50 health.")
    
    # Initial card draw
    for _ in range(5):
        player.draw_card(deck)
        opponent.draw_card(deck)

    # Game loop
    while player.health > 0 and opponent.health > 0:
        print(f"\n{player.name} Health: {player.health}, {opponent.name} Health: {opponent.health}")
        player.show_hand()
        player_choice = input("Choose a card to play (type index or 'q' to quit): ")
        
        if player_choice.lower() == 'q':
            print("Thanks for playing!")
            break

        try:
            player_card = player.play_card(int(player_choice))
            if player_card is None:
                continue
            
            # Simulate opponent play (basic AI for now)
            opponent_card = opponent.play_card(0)
            print(f"{opponent.name} plays {opponent_card}")

            apply_damage(player, opponent, player_card, opponent_card)
            
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
                break
            if player.health <= 0:
                print(f"{player.name} has fallen in battle.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
