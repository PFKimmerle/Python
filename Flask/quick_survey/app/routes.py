from flask import Blueprint, render_template, request, redirect, session

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form.get('comment', '')
    session['framework'] = request.form.getlist('framework')
    session['experience'] = request.form['experience']
    return redirect('/result')

@main.route('/result')
def result():
    return render_template('result.html')
