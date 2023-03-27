import requests
from bs4 import BeautifulSoup

# Get the page
url = 'https://magazin.photosynthesis.bg/bg/939-bezogledalni-fotoaparati'
page = requests.get(url)

# Parse the page
soup = BeautifulSoup(page.content, 'html.parser')

# Find all the product links
product_links = soup.find_all('a', class_='product_link')

# Write the product links to a text file
with open('productsFromPhotoSynthesis.txt', 'w', encoding="utf-8") as f:
    for link in product_links:
        f.write(link.get_text() + '\n')