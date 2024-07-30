import os
from flask import Flask, jsonify, request, render_template_string, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'books.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)

def init_db():
    with app.app_context():
        db.create_all()
        if not Book.query.first():
            books = [
                Book(title="Alice's Adventures in Wonderland", author="Lewis Carroll"),
                Book(title="Pride and Prejudice", author="Jane Austen"),
                Book(title="To Kill a Mockingbird", author="Harper Lee"),
                Book(title="1984", author="George Orwell"),
                Book(title="The Great Gatsby", author="F. Scott Fitzgerald")
            ]
            db.session.add_all(books)
            db.session.commit()
            print("Database initialized with sample books.")
        else:
            print("Database already contains books.")

@app.route('/')
def home():
    books = Book.query.all()
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Book API</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    </head>
    <body>
        <h1>Welcome to the Book API</h1>
        <h2>Book List</h2>
        <ul>
        {% for book in books %}
            <li>
                {{ book.title }} by {{ book.author }}
                <a href="{{ url_for('edit_book', id=book.id) }}">Edit</a>
                <form style="display:inline;" action="{{ url_for('delete_book', id=book.id) }}" method="post">
                    <input type="submit" value="Delete">
                </form>
            </li>
        {% endfor %}
        </ul>
        <h2>Add a New Book</h2>
        <form action="{{ url_for('add_book') }}" method="post">
            <input type="text" name="title" placeholder="Title" required>
            <input type="text" name="author" placeholder="Author" required>
            <input type="submit" value="Add Book">
        </form>
        <h2>API Endpoints</h2>
        <ul>
            <li><code>/books</code> (GET: List all books, POST: Add a new book)</li>
            <li><code>/books/&lt;id&gt;</code> (PUT: Update a book, DELETE: Remove a book)</li>
        </ul>
    </body>
    </html>
    ''', books=books)

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author} for book in books])

@app.route('/books', methods=['POST'])
def add_book():
    if request.is_json:
        data = request.json
    else:
        data = request.form
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({'error': 'Both title and author are required'}), 400
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    if request.is_json:
        return jsonify({'id': new_book.id, 'title': new_book.title, 'author': new_book.author}), 201
    return redirect(url_for('home'))

@app.route('/books/<int:id>', methods=['GET'])
def edit_book(id):
    book = Book.query.get_or_404(id)
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Edit Book</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    </head>
    <body>
        <h1>Edit Book</h1>
        <form action="{{ url_for('update_book', id=book.id) }}" method="post">
            <input type="text" name="title" value="{{ book.title }}" required>
            <input type="text" name="author" value="{{ book.author }}" required>
            <input type="submit" value="Update Book">
        </form>
        <a href="{{ url_for('home') }}">Back to Home</a>
    </body>
    </html>
    ''', book=book)

@app.route('/books/<int:id>', methods=['POST'])
def update_book(id):
    book = Book.query.get_or_404(id)
    if request.is_json:
        data = request.json
    else:
        data = request.form
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    db.session.commit()
    if request.is_json:
        return jsonify({'id': book.id, 'title': book.title, 'author': book.author})
    return redirect(url_for('home'))

@app.route('/books/<int:id>/delete', methods=['POST'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    if request.is_json:
        return '', 204
    return redirect(url_for('home'))

if __name__ == '__main__':
    os.makedirs(app.instance_path, exist_ok=True)
    init_db()
    app.run(debug=True)