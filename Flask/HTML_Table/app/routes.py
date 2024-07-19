from flask import current_app as app
from flask import render_template

@app.route('/')
def index():
    employees = [
        {'first_name': 'Alice', 'last_name': 'Smith', 'title': 'Software Engineer'},
        {'first_name': 'Bob', 'last_name': 'Johnson', 'title': 'Project Manager'},
        {'first_name': 'Charlie', 'last_name': 'Williams', 'title': 'UX Designer'},
        {'first_name': 'Dana', 'last_name': 'Brown', 'title': 'Data Scientist'}
    ]
    return render_template('index.html', employees=employees)
