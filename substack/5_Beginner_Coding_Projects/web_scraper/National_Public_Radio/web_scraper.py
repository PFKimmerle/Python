import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import csv
import time

def setup_driver():
    """Set up and return a Selenium WebDriver for Microsoft Edge."""
    options = webdriver.EdgeOptions()
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)
    return driver

def extract_headlines_and_details(driver, url):
    """Extract headlines and article details from the given URL."""
    driver.get(url)
    time.sleep(5)  # Wait for the page to load completely
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Update selectors based on the actual website structure
    articles = soup.find_all('a', href=True)
    
    # Debugging: Print the number of elements found
    print(f"Number of articles found: {len(articles)}")
    
    data = []
    for article in articles:
        title_tag = article.find('h3', class_='title')
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = article['href']
            
            # Extract description if available
            description_tag = article.find_next('p', class_='teaser')
            description = description_tag.get_text(strip=True) if description_tag else ''
            
            # Extract image URL if available
            image_tag = article.find('img')
            image_url = image_tag['src'] if image_tag else ''
            
            # Extract topic if available
            topic_tag = article.find_previous('h2', class_='slug')
            topic = topic_tag.get_text(strip=True) if topic_tag else ''
            
            data.append([title, link, description, image_url, topic])
    
    return data

def save_to_csv(data, filename):
    """Save the extracted data to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Title', 'URL', 'Description', 'Image URL', 'Topic'])
        writer.writerows(data)

if __name__ == "__main__":
    driver = setup_driver()
    try:
        url = "https://www.npr.org/"  # Replace with the actual news website URL
        data = extract_headlines_and_details(driver, url)
        save_to_csv(data, 'extracted_articles.csv')
        print("Data extraction and saving to CSV completed successfully.")
    finally:
        driver.quit()