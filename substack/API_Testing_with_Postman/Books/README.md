# Book API

This Flask-based Book API allows you to manage a collection of books. It provides a simple web interface and RESTful endpoints for creating, reading, updating, and deleting book records.

Check out my articles on my Substack website,[Pixels to Code](https://pfkimmerle.substack.com/).

## Features
- Web interface for managing books
- RESTful API endpoints for CRUD operations
- Search functionality for books by title or author
- SQLite database for data persistence

## Installation and Usage
To run on your local machine, follow these steps:

1. **Clone the Repository**
   - Clone this repository to your local machine: 'https://github.com/PFKimmerle/Python.git'
   - Navigate to the directory containing `Books`.

2. **Set Up a Virtual Environment** (Optional but recommended)
   - Create a virtual environment:'python -m venv venv'
   - Activate the virtual environment:
        - On Windows: venv\Scripts\activate
        - On Unix or MacOS: source venv/bin/activate

3. **Install Dependencies**
   - Install the required packages using:'pip install -r requirements.txt'

4. **Run the Application**
   - Start the application by running:'python app.py'
   - Access the web interface at `http://localhost:5000`.

# API Endpoints
- GET /books: List all books
- POST /books: Add a new book
- GET /books/<id>: Get a specific book
- PUT /books/<id>: Update a book
- DELETE /books/<id>: Remove a book
- GET /books/search?title=<title>&author=<author>: Search for books

# Usage with Postman
This API is ideal for testing with Postman. You can create collections for each endpoint and write tests to verify the API's functionality.

# License
This project is open source and available under the MIT License.