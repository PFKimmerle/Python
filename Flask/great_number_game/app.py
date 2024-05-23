from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
import random
import logging

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configure server-side session storage
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    if 'random_number' not in session or session['game_over']:
        session['random_number'] = random.randint(1, 100)
        session['guesses'] = []
        session['game_over'] = False
    logging.debug(f"Index page loaded. Random number: {session['random_number']}")
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if 'random_number' not in session:
        session['random_number'] = random.randint(1, 100)
        session['guesses'] = []
        session['game_over'] = False

    if session.get('game_over'):
        return redirect(url_for('index'))

    guess = int(request.form['guess'])
    random_number = session['random_number']
    guesses = session['guesses']
    guesses.append(guess)
    session['guesses'] = guesses

    logging.debug(f"New guess: {guess}. Random number: {random_number}. Guesses: {guesses}")

    if guess > random_number:
        message = "Too high!"
        color = "red"
    elif guess < random_number:
        message = "Too low!"
        color = "blue"
    else:
        message = "You got it!"
        color = "green"
        session['game_over'] = True

    return render_template('result.html', message=message, color=color, guesses=guesses, game_over=session['game_over'], random_number=random_number, attempts=len(guesses))

@app.route('/reset', methods=['POST'])
def reset():
    # Clear session data to start a new game
    session.pop('random_number', None)
    session.pop('guesses', None)
    session.pop('game_over', None)
    return redirect(url_for('index'))

@app.route('/add_to_leaderboard', methods=['POST'])
def add_to_leaderboard():
    name = request.form['name']
    attempts = request.form['attempts']
    leaderboard = session.get('leaderboard', [])
    leaderboard.append((name, int(attempts)))
    session['leaderboard'] = leaderboard
    # Clear session data after adding to the leaderboard
    session.pop('random_number', None)
    session.pop('guesses', None)
    session.pop('game_over', None)
    return redirect(url_for('leaderboard'))

@app.route('/leaderboard')
def leaderboard():
    leaderboard = session.get('leaderboard', [])
    return render_template('leaderboard.html', leaderboard=leaderboard)

if __name__ == '__main__':
    app.run(debug=True)
