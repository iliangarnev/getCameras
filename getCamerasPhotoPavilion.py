import requests
from bs4 import BeautifulSoup

# Get the page
url = 'https://photopavilion.bg/%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B8/%D1%83%D0%BF%D0%BE%D1%82%D1%80%D0%B5%D0%B1%D1%8F%D0%B2%D0%B0%D0%BD%D0%B0-%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B0/%D0%A4%D0%BE%D1%82%D0%BE%D0%B0%D0%BF%D0%B0%D1%80%D0%B0%D1%82%D0%B8-1/%D0%91%D0%B5%D0%B7%D0%BE%D0%B3%D0%BB%D0%B5%D0%B4%D0%B0%D0%BB%D0%BD%D0%B8-%D1%84%D0%BE%D1%82%D0%BE%D0%B0%D0%BF%D0%B0%D1%80%D0%B0%D1%82%D0%B8-3'
page = requests.get(url)

# Parse the page
soup = BeautifulSoup(page.content, 'html.parser')

# Find all the product links
product_links = soup.find_all('h1', class_='title')

# Write the product links to a text file
with open('productsFromPhotoPavilion.txt', 'w', encoding="utf-8") as f:
    for link in product_links:
        f.write(link.get_text() + '\n')