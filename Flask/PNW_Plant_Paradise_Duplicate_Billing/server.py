from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plants')
def plants():
    return render_template('plants.html')

@app.route('/checkout', methods=['POST'])
def checkout():
    fern = int(request.form.get('fern', 0))
    cactus = int(request.form.get('cactus', 0))
    bonsai = int(request.form.get('bonsai', 0))
    succulent = int(request.form.get('succulent', 0))
    first_name = request.form.get('first_name', '')
    last_name = request.form.get('last_name', '')
    student_id = request.form.get('student_id', '')
    
    total_plants = fern + cactus + bonsai + succulent
    print(f"Charging {first_name} {last_name} for {total_plants} plants")

    return render_template('checkout.html', fern=fern, cactus=cactus, bonsai=bonsai, succulent=succulent, first_name=first_name, last_name=last_name, student_id=student_id)

if __name__ == '__main__':
    app.run(debug=True)
