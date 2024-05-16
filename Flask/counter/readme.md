# Counter Flask Application

## Overview

The Counter Flask Application is a simple web application designed to track the number of times a user has visited the site. It provides basic functionality to increment a counter, reset it, and allows custom increments specified by the user.

## Detailed Descriptions

### Main Application (app.py)

**Functionality**:
- Initializes the Flask application and sets up session management.
- Defines the root route to display the counter and visit count.
- Provides routes to increment the counter by 2, reset the counter, and increment by a custom value.

**Parameters**:
- `visit_count`: Tracks the number of times the user has visited the site.
- `counter_value`: Stores the current value of the counter.

### HTML Template (index.html)

**Functionality**:
- Provides the user interface for the counter application.
- Displays the visit count and counter value.
- Includes forms and buttons to increment the counter, reset it, and specify custom increments.

**Parameters**:
- `{{ visit_count }}`: The Jinja2 variable to display the visit count.
- `{{ counter_value }}`: The Jinja2 variable to display the counter value.

### CSS Styles (styles.css)

**Functionality**:
- Defines the styles for the HTML elements to create a visually appealing user interface.
- Styles the buttons for incrementing and resetting the counter with distinct colors.
- Centers the text and elements on the page for a modern, clean look.

**Parameters**:
- `body`: Sets the overall font, text alignment, margin, background color, and text color.
- `h1`: Styles the main heading with font size and color.
- `#counter`: Styles the counter display with font size and margin.
- `button`: Styles the buttons with font size, margin, padding, border, border-radius, cursor, and transition effects.
- `button#increment`: Sets the background color and hover effect for the increment button.
- `button#reset`: Sets the background color and hover effect for the reset button.
- `form`: Styles the form elements with display, margin, padding, border, and border-radius.

### Form Handling (Forms within index.html)

**Functionality**:
- Handles user input to increment the counter by a specified value.
- Processes form submissions to update the counter value based on user input.

**Parameters**:
- `increment`: The input field for specifying the custom increment value.
- `submit`: The button to submit the custom increment form.

## Getting Started
To use Counter Flask Application, follow these steps:
1. Clone the repository from GitHub to your local machine: git clone 'https://github.com/PFKimmerle/Python/tree/main'
2. Navigate to the project directory.
3. Install dependencies: 'pip install -r requirements.txt'
4. Run the Flask application: 'python app.py'


## Installation Guide
Install follow these steps:
1. Ensure Python 3.8 or higher is installed.
2. Clone the project as shown above.
3. Navigate to the project directory and install the required Python packages.


## Resources
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Jinja Templating](https://jinja.palletsprojects.com/en/3.0.x/)
- [Python Documentation](https://docs.python.org/3/)

## License Information
The project is licensed under MIT License. See the LICENSE file in the repository for more details.