# Web Scraper

This project is a Python-based web scraper designed to extract headlines and article details from a news website using Selenium and BeautifulSoup. The extracted data is saved into a CSV file for easy handling and analysis.

## Introduction

The Web Scraper automates the process of navigating to the National Public Radio (NPR) website, extracting article details such as titles, URLs, descriptions, image URLs, and topics, and saving them into a CSV file. This tool is useful for data analysis, media monitoring, and research purposes.

## Features

- **Automated Web Scraping**: Utilizes Selenium to automate browser interaction and BeautifulSoup to parse HTML content.
- **CSV Output**: Saves the extracted data into a CSV file, making it easy to import and analyze in various data processing tools.

## Requirements

- Python 3.7 or higher
- Microsoft Edge browser
- The following Python packages:
  - `selenium`
  - `webdriver_manager`
  - `beautifulsoup4`
  - `lxml`

## Installation

Follow these steps to set up and run the Web Scraper:

1. Clone the Repository: `https://github.com/PFKimmerle/Python.git`
2. Set up a Virtual Environment: `python -m venv venv`
3. Activate the Virtual Environment
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. Install Dependencies: `pip install -r requirements.txt`
5. Run the Web Scraper: `python web_scraper.py`

## Expected Output

The script will navigate to the NPR homepage, extract article details, and save them to `extracted_articles.csv`.

## Customizing Wait Time

The default wait time for page loading is 5 seconds. You can adjust this by modifying the `time.sleep(5)` line in the `extract_headlines_and_details` function.

## Note on Using Different Websites

If you choose to scrape a different website, you may encounter issues such as:
- Different HTML structures that require changes in the BeautifulSoup parsing logic.
- Additional or missing elements that need to be handled.
- Different loading times that may require adjustments in the wait time.

## Output

The output is a CSV file named `extracted_articles.csv` containing the following columns:

- `Title`: The headline of the article
- `URL`: The URL of the article
- `Description`: A brief description of the article
- `Image URL`: The URL of the article's image
- `Topic`: The topics associated with the article

## Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
- [Learn Python Programming](https://www.learnpython.org/)

## License

This project is licensed under the MIT License. For more details, see the license file in the repository.