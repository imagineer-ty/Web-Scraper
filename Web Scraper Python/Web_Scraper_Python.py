import requests
from bs4 import BeautifulSoup
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# List of URLs to scrape
urls = [
    'https://www.news4jax.com/weather/',
    'https://www.news4jax.com/news/'
    # Add more URLs as needed
]

# Function to scrape titles from a given URL
def scrape_titles(url):
    try:
        # Send a GET request to the website with SSL verification disabled
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all article titles (assuming they are in <h2> tags)
        titles = soup.find_all('h2')
        
        # Print the titles
        for title in titles:
            print(title.get_text())

    except requests.exceptions.RequestException as e:
        # Handle any requests exceptions (e.g., network issues, invalid URL, etc.)
        print(f"An error occurred while making the request to {url}: {e}")

    except Exception as e:
        # Handle any other exceptions
        print(f"An unexpected error occurred while processing {url}: {e}")

# Scrape titles from all URLs
for url in urls:
    scrape_titles(url)
