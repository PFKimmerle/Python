# PNW Plant Paradise

PNW Plant Paradise is a project created to practice using Flask for building a web application. The primary educational goal of this project is to demonstrate how to handle form submissions using POST requests and to highlight the potential issues with rendering HTML directly on a URL that received a POST request.

### Purpose of the Project
The main goal of this project is to:
1. **Collect Data via Form**: Implement a form where users can input data, such as selecting plants and entering personal information.
2. **Handle POST Request**: Process the form data on the server side and redirect to another URL to display the result.
3. **Demonstrate Issues with Rendering on POST**: Rendering HTML directly in response to a POST request can cause issues such as double submissions if the user refreshes the page. This can lead to unintended actions like duplicate transactions. To avoid this, it's better to handle the POST request, process the data, and then redirect to a new URL, where a GET request can render the HTML. This approach prevents double submissions and ensures proper state management.

### Main Functionality
- **Browse Plants**: Users can view a variety of plants, each with detailed descriptions and images.
- **Order Plants**: Users can select the quantity of plants they wish to purchase and fill out their information for order processing.
- **Order Confirmation**: After placing an order, users receive a confirmation message with the details of their purchase.


## Getting Started
To use PNW Plant Paradise, follow these steps:
1. Clone the repository from GitHub to your local machine.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the web application: `python server.py`

## Installation Guide
Install PNW Plant Paradise by following these steps:
1. Ensure Python 3.8 or higher is installed.
2. Clone the project as shown above.
3. Navigate to the project directory and install the required Python packages.

## Resources

List of helpful resources or reading materials:
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Documentation](https://docs.python.org/3/)

## License Information

The project is licensed under MIT License. See the LICENSE file in the repository for more details.
