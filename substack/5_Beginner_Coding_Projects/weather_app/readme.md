# Weather App
A simple Python script to fetch the current weather for a given city or zip code using the wttr.in service.

## Features
- Fetches weather information for any given city or zip code.
- Provides a concise weather summary including temperature and weather conditions.
- Handles HTTP errors gracefully.

## Requirements
- Python 3.x
- `requests` library
- `BeautifulSoup` library (though not strictly necessary with the current implementation)

## Note

If you encounter an error while using the weather service, please check the [wttr.in website](https://wttr.in) directly. The site may be down or experiencing issues, which could lead to errors that are not related to your code.


## Installation
1. Clone the repository: 'https://github.com/PFKimmerle/Python.git'
2. Install the required Python libraries: 'pip install requests beautifulsoup4'
3. Install Dependencies: 'pip install requests beautifulsoup4'


## Usage
Run the script: 'python weather_app.py'


## Expected Output
Enter the city or zip code for the weather: 98045
78108: ☀️   +20°C


## License
This project is licensed under the MIT License. 

## Acknowledgments
wttr.in for the weather service.