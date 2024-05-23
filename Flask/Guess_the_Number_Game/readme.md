## Guess the Number Game

Welcome to the "Guess the Number" game project! This is a beginner-level Python Flask application where players guess a randomly selected number between 1 and 100.

## Project Structure

The project is structured as follows:
- `app.py`: The main Flask application file.
- `static/`: Contains static files such as CSS.
- `templates/`: Contains HTML template files.

## Features

- **Random Number Generation**: The game generates a random number between 1 and 100.
- **Guessing Mechanism**: Players can input their guesses and receive feedback whether the guess is too high, too low, or correct.
- **Leaderboard**: Tracks the number of attempts taken by players to guess the correct number and displays the leaderboard.

## Setup and Installation

1. Clone the repository:git clone https://github.com/PFKimmerle/Python.git
2. Create a virtual environment and install dependencies: 
'python3 -m venv venv' 
'source venv/bin/activate'
'pip install -r requirements.txt'
3. Run the application: 'flask run'
4. Open your web browser and go to http://127.0.0.1:5000/


## How to Play

1. Start the Game: Open the application in your browser.
2. Guess the Number: Enter a number between 1 and 100 and submit your guess.
3. Receive Feedback: The game will tell you if your guess is too high, too low, or correct.
4. Track Your Attempts: The game keeps track of the number of attempts you have made.
5. Leaderboard: Once you guess the correct number, you can enter your name to save your score on the leaderboard.


## Files

- app.py: Contains the main Flask application code.
- index.html: The main page where users can enter their guesses.
- result.html: Displays the result of the guess and provides feedback.
- leaderboard.html: Shows the leaderboard with names and attempts.
- styles.css: Contains the styling for the HTML pages.


## License

This project is licensed under the MIT License. See the LICENSE file for more details.

