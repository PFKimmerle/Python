from flask import Flask, session, redirect, url_for, render_template, request

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session management

@app.route('/')
def index():
    if 'visit_count' not in session:
        session['visit_count'] = 0
    if 'counter_value' not in session:
        session['counter_value'] = 0
    session['visit_count'] += 1
    return render_template('index.html', visit_count=session['visit_count'], counter_value=session['counter_value'])

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

@app.route('/increment_by_two', methods=['POST'])
def increment_by_two():
    if 'counter_value' not in session:
        session['counter_value'] = 0
    session['counter_value'] += 2
    return redirect(url_for('index'))

@app.route('/custom_increment', methods=['POST'])
def custom_increment():
    increment = int(request.form.get('increment', 1))
    if 'counter_value' not in session:
        session['counter_value'] = 0
    session['counter_value'] += increment
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
