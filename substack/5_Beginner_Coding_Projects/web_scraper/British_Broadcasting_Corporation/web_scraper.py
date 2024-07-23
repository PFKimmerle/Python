import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import time

def setup_driver():
    """Set up and return a Selenium WebDriver."""
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def extract_page_data(driver, url, wait_time=10):
    """Navigate to the given URL and return the parsed BeautifulSoup object."""
    driver.get(url)
    time.sleep(wait_time)  # Wait for the page to load and JavaScript to render
    return BeautifulSoup(driver.page_source, 'html.parser')

def find_next_data_script(soup):
    """Find and return the JSON data from the __NEXT_DATA__ script tag."""
    script_tag = soup.find('script', id='__NEXT_DATA__')
    if script_tag:
        return json.loads(script_tag.string)
    else:
        raise ValueError("Script tag with id '__NEXT_DATA__' not found")

def parse_articles(json_data):
    """Parse and return a list of articles from the given JSON data."""
    try:
        props = json_data['props']
        pageProps = props['pageProps']
        page = pageProps['page']

        articles = []
        unusual_key = '@"news",'
        if unusual_key in page:
            sections = page[unusual_key].get('sections', [])
            for section in sections:
                for content in section.get('content', []):
                    if 'title' in content:
                        article = {
                            'title': content['title'],
                            'url': "https://www.bbc.com" + content.get('href', ''),
                            'description': content.get('description', ''),
                            'image_url': content.get('image', {}).get('model', {}).get('blocks', {}).get('src', ''),
                            'topics': content.get('metadata', {}).get('topics', [])
                        }
                        articles.append(article)
        return articles
    except KeyError as e:
        raise KeyError(f"KeyError: {e}")

def save_to_csv(articles, filename):
    """Save the list of articles to a CSV file."""
    keys = articles[0].keys() if articles else []
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(articles)

def main():
    """Main function to run the web scraper and save extracted articles to a CSV file."""
    driver = setup_driver()
    try:
        soup = extract_page_data(driver, "https://www.bbc.com/news")
        json_data = find_next_data_script(soup)
        articles = parse_articles(json_data)

        if articles:
            save_to_csv(articles, 'extracted_articles.csv')
            print(f"Saved {len(articles)} articles to 'extracted_articles.csv'")
        else:
            print("No articles found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
