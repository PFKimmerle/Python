from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/plants')
def plants():
    return render_template("plants.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    # Retrieve form data
    fern = int(request.form.get('fern', 0))
    cactus = int(request.form.get('cactus', 0))
    bonsai = int(request.form.get('bonsai', 0))
    succulent = int(request.form.get('succulent', 0))
    first_name = request.form.get('first_name', 'Sabri')
    last_name = request.form.get('last_name', 'Garcia')
    student_id = request.form.get('student_id', '')

    # Calculate total plants
    total_plants = fern + cactus + bonsai + succulent
    
    # Print statement to terminal
    print(f"Charging {first_name} {last_name} for {total_plants} plants")

    # Store data in session
    session['checkout_data'] = {
        'fern': fern,
        'cactus': cactus,
        'bonsai': bonsai,
        'succulent': succulent,
        'first_name': first_name,
        'last_name': last_name,
        'student_id': student_id
    }

    # Redirect to GET request
    return redirect(url_for('show_checkout'))

@app.route('/checkout')
def show_checkout():
    data = session.get('checkout_data', {})
    # Ensure default values if no data provided
    if not data.get('first_name'):
        data['first_name'] = 'Sabri'
    if not data.get('last_name'):
        data['last_name'] = 'Garcia'
    return render_template('checkout.html', **data)

if __name__ == '__main__':
    app.run(debug=True)
