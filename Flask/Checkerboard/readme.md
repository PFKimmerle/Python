
## Overview

The Checkerboard Flask Application is a simple web application that renders a customizable checkerboard.

### Application Functionality

**Functionality**:
- Initializes the Flask application and sets up routes to render the checkerboard.
- Defines the root route to render an 8x8 checkerboard.
- Provides routes to render a checkerboard of size 8x`x`, `x`x`y`, and with custom colors.

**Parameters**:
- `x`: The number of columns for the checkerboard.
- `y`: The number of rows for the checkerboard.
- `color1`: The first color for the checkerboard.
- `color2`: The second color for the checkerboard.

### HTML Template (index.html)

**Functionality**:
- Provides the user interface for the checkerboard application.
- Displays the checkerboard based on the provided parameters.
- Includes forms and inputs to customize the size and colors of the checkerboard.

### CSS Styles (styles.css)

**Functionality**:
- Defines the styles for the HTML elements to create a visually appealing checkerboard.
- Styles the checkerboard cells with distinct colors.
- Centers the text and elements on the page for a clean look.


## Getting Started

To use the Checkerboard Flask Application, follow these steps:
1. Clone the repository from GitHub to your local machine: git clone 'https://github.com/PFKimmerle/Python.git'
2. Navigate to the project directory.
3. Install dependencies: 'pip install -r requirements.txt'
4. Run the Flask application: 'python run.py'

## Installation Guide

Follow these steps:
1. Ensure Python 3.8 or higher is installed.
2. Clone the project as shown above.
3. Navigate to the project directory and install the required Python packages.

## Usage

1. **Render the default 8x8 checkerboard**:
    Open a browser and go to: `http://127.0.0.1:5000/`

2. **Render a checkerboard of size 8xX**:
    Open a browser and go to: `http://127.0.0.1:5000/4` (replace `4` with any number)

3. **Render a checkerboard of size XxY**:
    Open a browser and go to: `http://127.0.0.1:5000/5/10` (replace `5` and `10` with any numbers)

4. **Render a checkerboard with custom colors**:
    Open a browser and go to: `http://127.0.0.1:5000/5/10/yellow/red/` (replace `5`, `10`, `yellow`, and `red` with any numbers and colors)

## License Information

The project is licensed under MIT License. See the LICENSE file in the repository for more details.
