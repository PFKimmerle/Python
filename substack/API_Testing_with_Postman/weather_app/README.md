
# Weather App (Postman Practice)

This simple Flask-based weather app is designed for practicing API testing with Postman. It generates mock weather data for a specified city. Please note that this app does not provide real weather forecasts and is intended for educational purposes only.

Check out my articles on my Substack website,[Pixels to Code](https://pfkimmerle.substack.com/).

## Features
- Generate and display mock weather information based on user input (city name).
- Demonstrate basic API endpoint creation and response handling.
- Provide a simple web interface for interacting with the API.

## Installation and Usage
To run the Weather App on your local machine, follow these steps:

1. **Clone the Repository**
   - Clone this repository to your local machine: 'https://github.com/PFKimmerle/Python.git'
   - Navigate to the directory containing `weather_app`.

2. **Set Up a Virtual Environment** (Optional but recommended)
   - Create a virtual environment:'python -m venv venv'
   - Activate the virtual environment:
        - On Windows: venv\Scripts\activate
        - On Unix or MacOS: source venv/bin/activate

3. **Install Dependencies**
   - Install the required packages using:'pip install -r requirements.txt'

4. **Run the Application**
   - Start the application by running:'python weather_app.py'
   - Access the web interface at `http://localhost:5000`.

# API Endpoint
- GET /weather?city=<city_name>: Returns mock weather data for the specified city.

# Using with Postman
This app is designed to be used with Postman for API testing practice. You can create various requests to test different scenarios and practice writing test scripts in Postman.

## License
This project is licensed under the MIT License. For more details, see the LICENSE file in the repository.
