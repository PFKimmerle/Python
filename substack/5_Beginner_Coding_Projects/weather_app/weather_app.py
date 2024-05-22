import requests
from bs4 import BeautifulSoup

def get_weather(city_or_zip):
    base_url = "https://wttr.in/"
    complete_url = base_url + city_or_zip + "?format=3"

    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        print(response.text.strip())
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    city_or_zip = input("Enter the city or zip code for the weather: ")
    get_weather(city_or_zip)
