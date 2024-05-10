import random

def introduction():
    print("Welcome to Elemental Showdown!")
    print("In a world torn by elemental forces, two beings emerge as leaders of their factions.")
    print("One, a Hero seeking to bring peace. The other, a Villain, driven by the chaos of power.")
    print("Choose your side and battle using the elemental cards to either save or dominate the world.\n")

def create_cards():
    return {
        'Fire': 10,
        'Water': 8,
        'Earth': 6,
        'Air': 4
    }

def play_turn(player, cards):
    if player == "Player":
        print("\nAvailable cards:")
        for card, damage in cards.items():
            print(f"{card} card: {damage} damage")
        card_choice = input("Choose a card to play (type the element name): ")
        damage = cards.get(card_choice.title(), 0)  # Default to 0 damage if an invalid card is chosen
        if damage == 0:
            print("Invalid card choice. Lost your turn!")
        else:
            print(f"{player} plays a {card_choice.title()} card dealing {damage} damage!")
    else:
        card, damage = random.choice(list(cards.items()))
        print(f"{player} draws a {card} card dealing {damage} damage!")
    return damage

def game_loop(player_health, ai_health, cards, ai_role):
    turn = 0  # 0 for player, 1 for AI
    while player_health > 0 and ai_health > 0:
        if turn == 0:
            print("\nPlayer's turn:")
            damage = play_turn("Player", cards)
            ai_health -= damage
            turn = 1
        else:
            print(f"\n{ai_role}'s turn:")
            damage = play_turn(ai_role, cards)
            player_health -= damage
            turn = 0
        print(f"Player Health: {player_health}, {ai_role} Health: {ai_health}")
        
    if player_health <= 0:
        print(f"{ai_role} wins!")
    else:
        print("Player wins!")

def main():
    introduction()
    choice = input("Choose your character:\n1. Hero\n2. Villain\nSelect your character (1-2): ")
    player_role = 'Hero' if choice == '1' else 'Villain'
    ai_role = 'Villain' if choice == '1' else 'Hero'
    cards = create_cards()
    player_health = 50
    ai_health = 50
    game_loop(player_health, ai_health, cards, ai_role)

if __name__ == "__main__":
    main()
