# Web Scraper

This project is a Python-based web scraper designed to extract headlines and article details from the a news website using Selenium and BeautifulSoup. The extracted data is saved into a CSV file for easy handling and analysis.


## Introduction

The Web Scraper automates the process of navigating to the British Broadcasting Corporation (BBC) News website, extracting article details such as titles, URLs, descriptions, image URLs, and topics, and saving them into a CSV file. This tool is useful for data analysis, media monitoring, and research purposes.

## Features

- **Automated Web Scraping**: Utilizes Selenium to automate browser interaction and BeautifulSoup to parse HTML content.
- **JSON Data Extraction**: Extracts data from the `__NEXT_DATA__` script tag, ensuring accurate and structured data retrieval.
- **CSV Output**: Saves the extracted data into a CSV file, making it easy to import and analyze in various data processing tools.

## Requirements

- Python 3.7 or higher
- Google Chrome browser
- The following Python packages:
  - `selenium`
  - `webdriver_manager`
  - `beautifulsoup4`
  - `lxml`

## Installation
Follow these steps to set up and run the Web Scraper:
1. Clone the Repository: 'https://github.com/PFKimmerle/Python.git'
2. Set up a Virtual Environment: 'python -m venv venv'
3. Activate the Virtual Environment
- On Windows: 'venv\Scripts\activate'
- On macOS/Linux: 'source venv/bin/activate'
4. Install Dependencies 'pip install -r requirements.txt'
5. Run the Web Scraper 'python web_scraper.py'


## Expected Output
The script will navigate to the BBC News homepage, extract article details, and save them to 'extracted_articles.csv'.

## Customizing Wait Time
The default wait time for page loading is 10 seconds. You can adjust this by modifying the wait_time parameter in the extract_page_data function call.

## Output
The output is a CSV file named extracted_articles.csv containing the following columns:
- title: The headline of the article
- url: The URL of the article
- description: A brief description of the article
- image_url: The URL of the article's image
- topics: The topics associated with the article

## Resources
- [Python Official Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
- [Learn Python Programming](https://www.learnpython.org/)

## License
This project is licensed under the MIT License. For more details, see the license file in the repository.