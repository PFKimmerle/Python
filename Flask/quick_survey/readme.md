# Quick Survey

Quick Survey is a simple Flask application that collects survey data through a form and displays the results.

## Installation

1. Clone the repository:  'https://github.com/PFKimmerle/Python.git'
2. Change to the project directory: 'cd quicksurvey'
3. Create a virtual environment: 'python3 -m venv venv'
4. Activate the virtual environment:
- On Unix-like systems (Linux, macOS): 'source venv/bin/activate'
- On Windows, use: 'venv\Scripts\activate'
5. Install the dependencies: 'pip install -r requirements.txt'


## Usage

1. Run the application:'python run.py'
2. Open your browser and navigate to `http://localhost:5000`.

## Project Structure

- `app/`: Contains the main application code.
  - `__init__.py`: Initializes the Flask application.
  - `routes.py`: Contains the routes and view functions.
  - `static/`: Contains static files such as CSS.
    - `style.css`: Custom styles for the application.
  - `templates/`: Contains HTML templates.
    - `index.html`: The main form page.
    - `result.html`: The page displaying submitted data.
- `venv/`: Virtual environment directory.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: Provides information about the project.
- `requirements.txt`: Lists the project dependencies.
- `run.py`: Entry point to run the Flask application.

## Features

- Simple form to collect survey data.
- Displays the submitted data on a results page.
- Styled using Bootstrap for a modern and responsive design.

## License

This project is licensed under the MIT License.

