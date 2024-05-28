# Elemental Showdown

Elemental Showdown is a text-based card game where players choose to be either a Hero or a Villain, using elemental cards to battle against a computer-controlled opponent . The goal is to reduce the opponent's health to zero using strategic card plays that leverage elemental strengths and weaknesses.

## Versions

This repository contains two versions of the game:

### Version 1: Modular Approach
This version of the game is split into multiple modules, making the code easier to maintain and extend. The structure includes separate files for cards, players, the deck, and game mechanics.

- `card.py`: Defines the `Card` class, which represents the elemental cards used in the game.
- `deck.py`: Defines the `Deck` class that manages the collection of cards.
- `player.py`: Contains the `Player` class for managing each player's hand, health, and actions.
- `game.py`: Contains the main game logic and interactions with the user.

### Version 2: Single File Approach
This version simplifies the entire game into a single Python file, `main.py`. It is designed for quick setup and easier handling for smaller projects or demonstrations.

- `main.py`: Includes all game components integrated into a single file. This includes card, deck, and player definitions, along with the main game loop.

## Features
- Choose between Hero and Villain roles.
- Engage in battles using cards that represent elements like Fire, Water, Earth, and Air.
- Elemental effectiveness influences the outcome of battles, making strategic card selection important.
- Interactive gameplay with a simple text-based interface.


## Usage Instructions

To play **Elemental Showdown**, follow these steps:
1. Clone the repository: `https://github.com/PFKimmerle/Python/tree/main/Fundamentals/games`
2. Navigate to the `elemental_showdown` directory.
3. Depending on the version you want to play:
   - For Version 1, run: `python game.py`
   - For Version 2, run: `python main.py`
4. Enjoy battling between heroes and villains using elemental powers.

## License
This project is licensed under the MIT License.