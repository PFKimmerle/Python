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
                Book(title="API Recipes: Cook Up Perfect Requests", author="Pink Ducky"),
                Book(title="Developer's Delight: Quacking Good API Tips", author="Blue Rubber Duck"),
                Book(title="HTTP for Hungry Coders", author="Yellow Canary"),
                Book(title="Debugging with Ducky", author="Black Duck"),
                Book(title="The Quirky Query Cookbook", author="Rainbow Duck"),
                Book(title="Glitter Duck's Guide to APIs", author="Glitter Rubber Duck"),
                Book(title="Waddle Through RESTful Services", author="Shiny Blue Duck"),
                Book(title="Postman Adventures: A Duck's Journey", author="Adventurous Duck"),
                Book(title="The Rubber Duck's API Playbook", author="Playful Duck"),
                Book(title="Quack-tastic REST API Tricks", author="Quirky Yellow Duck")
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
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <style>
            body {
                font-size: 14px;
                max-width: 1000px;
                margin: 0 auto;
                padding: 20px;
            }
            h1 { font-size: 24px; }
            h2 { font-size: 20px; }
            input[type="text"], input[type="submit"] {
                font-size: 14px;
                padding: 5px;
                margin-bottom: 10px;
            }
            .api-endpoint {
                background-color: #f8f8f8;
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 10px;
                margin-bottom: 10px;
            }
            .api-endpoint code {
                font-weight: bold;
            }
            .api-endpoint p {
                margin: 5px 0 0 0;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the Book API</h1>

        <h2>Book List</h2>
        <ul id="bookList">
        {% for book in books %}
            <li>
                {{ book.title }} by {{ book.author }}
                <a href="{{ url_for('edit_book', id=book.id) }}">Edit</a>
                <button class="delete-book" data-id="{{ book.id }}">Delete</button>
            </li>
        {% endfor %}
        </ul>

        <h2>Add a New Book</h2>
        <form id="addBookForm">
            <input type="text" name="title" placeholder="Title" required>
            <input type="text" name="author" placeholder="Author" required>
            <input type="submit" value="Add Book">
        </form>

        <h2>API Endpoints</h2>
        <div class="api-endpoint">
            <code>/books</code>
            <p>GET: List all books, POST: Add a new book</p>
        </div>
        <div class="api-endpoint">
            <code>/books/&lt;id&gt;</code>
            <p>GET: Get a specific book, PUT: Update a book, DELETE: Remove a book</p>
        </div>
        <div class="api-endpoint">
            <code>/books/search?title=&lt;title&gt;&author=&lt;author&gt;</code>
            <p>GET: Search for a book</p>
        </div>

        <script>
        $(document).ready(function() {
            $("#addBookForm").submit(function(e) {
                e.preventDefault();
                var formData = {
                    title: $("input[name='title']").val(),
                    author: $("input[name='author']").val()
                };
                $.ajax({
                    url: "{{ url_for('add_book') }}",
                    type: "POST",
                    contentType: "application/json",
                    data: JSON.stringify(formData),
                    success: function(response) {
                        alert("Book added successfully!");
                        location.reload();
                    },
                    error: function(error) {
                        alert("Error adding book: " + error.responseJSON.error);
                    }
                });
            });

            $(document).on("click", ".delete-book", function() {
                var bookId = $(this).data("id");
                if (confirm("Are you sure you want to delete this book?")) {
                    $.ajax({
                        url: "/books/" + bookId,
                        type: "DELETE",
                        success: function(response) {
                            alert("Book deleted successfully!");
                            location.reload();
                        },
                        error: function(error) {
                            alert("Error deleting book: " + error.responseJSON.error);
                        }
                    });
                }
            });
        });
        </script>
    </body>
    </html>
    ''', books=books)

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author} for book in books])

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({'error': 'Both title and author are required'}), 400
    new_book = Book(title=data['title'], author=data['author'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'id': new_book.id, 'title': new_book.title, 'author': new_book.author}), 201

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({'id': book.id, 'title': book.title, 'author': book.author})

@app.route('/books/search', methods=['GET'])
def search_book():
    title = request.args.get('title')
    author = request.args.get('author')
    query = Book.query
    if title:
        query = query.filter(Book.title.ilike(f'%{title}%'))
    if author:
        query = query.filter(Book.author.ilike(f'%{author}%'))
    books = query.all()
    if books:
        return jsonify([{'id': book.id, 'title': book.title, 'author': book.author} for book in books])
    else:
        return jsonify({'error': 'No books found'}), 404

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.json
    if 'title' in data:
        book.title = data['title']
    if 'author' in data:
        book.author = data['author']
    db.session.commit()
    return jsonify({'id': book.id, 'title': book.title, 'author': book.author})

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted'}), 200

@app.route('/books/<int:id>/edit', methods=['GET'])
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
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    </head>
    <body>
        <h1>Edit Book</h1>
        <form id="editBookForm">
            <input type="text" name="title" value="{{ book.title }}" required>
            <input type="text" name="author" value="{{ book.author }}" required>
            <input type="submit" value="Update Book">
        </form>
        <a href="{{ url_for('home') }}">Back to Home</a>

        <script>
        $(document).ready(function() {
            $("#editBookForm").submit(function(e) {
                e.preventDefault();
                var formData = {
                    title: $("input[name='title']").val(),
                    author: $("input[name='author']").val()
                };
                $.ajax({
                    url: "{{ url_for('update_book', id=book.id) }}",
                    type: "PUT",
                    contentType: "application/json",
                    data: JSON.stringify(formData),
                    success: function(response) {
                        alert("Book updated successfully!");
                        window.location.href = "{{ url_for('home') }}";
                    },
                    error: function(error) {
                        alert("Error updating book: " + error.responseJSON.error);
                    }
                });
            });
        });
        </script>
    </body>
    </html>
    ''', book=book)

if __name__ == '__main__':
    os.makedirs(app.instance_path, exist_ok=True)
    init_db()
    app.run(debug=True)