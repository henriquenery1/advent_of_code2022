# make a code in python to build a basic web scraper that can extract data from a website and store it in a structured format

# Import the BeautifulSoup library
from bs4 import BeautifulSoup

# Import the request library
import requests

# Make a GET request to the website you want to scrape
response = requests.get('http://www.example.com')

# Parse the HTML of the website using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the data you want to scrape from the HTML using BeautifulSoup's methods
data = soup.find('div', class_='data-container')

# Store the data in a structured format, such as a dictionary or list
structured_data = {}
for item in data:
  structured_data[item.name] = item.value

# Print the structured data to the console
print(structured_data)
