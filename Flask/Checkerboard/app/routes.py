from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('checkerboard.html', width=10, height=10, color1="white", color2="black")

@app.route('/4')
def four():
    return render_template('checkerboard.html', width=10, height=4, color1="white", color2="black")

@app.route('/<height>/<width>')
def h_and_w(height, width):
    return render_template('checkerboard.html', width=int(width), height=int(height), color1="white", color2="black")

@app.route('/<h>/<w>/<colorOne>/<colorTwo>/')
def h_and_w_with_color(h, w, colorOne, colorTwo):
    return render_template('checkerboard.html', width=int(w), height=int(h), color1=colorOne, color2=colorTwo)
