from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a real secret key

def get_gold(place):
    gold_mapping = {
        'island': random.randint(10, 20),
        'cave': random.randint(5, 10),
        'hut': random.randint(2, 5),
        'casino': random.randint(-50, 50)
    }
    return gold_mapping.get(place, 0)

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
        session['moves'] = 0
        session['game_over'] = False
    return render_template('index.html', gold=session['gold'], activities=session['activities'], game_over=session['game_over'])

@app.route('/process_money', methods=['POST'])
def process_money():
    if session.get('game_over', False):
        return redirect('/')
    
    place = request.form['place']
    gold_earned = get_gold(place)
    session['gold'] += gold_earned
    session['moves'] += 1

    color = 'green' if gold_earned >= 0 else 'red'
    activity = {
        'text': f"Earned {gold_earned} gold from the {place}! ({datetime.now().strftime('%Y/%m/%d %H:%M:%S')})",
        'color': color
    }
    session['activities'].insert(0, activity)

    print(f"Current gold: {session['gold']}, Moves: {session['moves']}")  # Debug print

    if session['gold'] >= 500 or session['moves'] >= 15:
        session['game_over'] = True
        print("Game Over!")  # Debug print

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
