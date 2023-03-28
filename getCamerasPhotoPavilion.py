"""
import requests
from bs4 import BeautifulSoup
import os

url = 'https://photopavilion.bg/%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B8/%D1%83%D0%BF%D0%BE%D1%82%D1%80%D0%B5%D0%B1%D1%8F%D0%B2%D0%B0%D0%BD%D0%B0-%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B0/%D0%A4%D0%BE%D1%82%D0%BE%D0%B0%D0%BF%D0%B0%D1%80%D0%B0%D1%82%D0%B8-1/%D0%91%D0%B5%D0%B7%D0%BE%D0%B3%D0%BB%D0%B5%D0%B4%D0%B0%D0%BB%D0%BD%D0%B8-%D1%84%D0%BE%D1%82%D0%BE%D0%B0%D0%BF%D0%B0%D1%80%D0%B0%D1%82%D0%B8-3'  # Replace with the actual URL
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")
products = soup.find_all('h1', class_='title')

product_links = []

for product in products:
    link = product.find("a")["href"]
    product_links.append(link)

# Read the previously saved product links from the text file (if it exists)
previous_product_links = []
file_name = "productsFromPhotoPavilion.txt"

if os.path.exists(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        previous_product_links = [line.strip() for line in file.readlines()]

# Compare the current list of product links with the previously saved list
if set(product_links) != set(previous_product_links):
    # If there are any changes, write the new list to the text file
    with open(file_name, "w", encoding="utf-8") as file:
        for link in product_links:
            file.write(f"{link}\n")
    print("Product links updated.")
else:
    print("No changes in product links.")
"""
from bs4 import BeautifulSoup
import requests
import os
import asyncio
from telegram import Bot
from dotenv import load_dotenv
load_dotenv()

async def main():
    url = 'https://photopavilion.bg/%D0%BF%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B8/%D1%83%D0%BF%D0%BE%D1%82%D1%80%D0%B5%D0%B1%D1%8F%D0%B2%D0%B0%D0%BD%D0%B0-%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B0/%D0%A4%D0%BE%D1%82%D0%BE%D0%B0%D0%BF%D0%B0%D1%80%D0%B0%D1%82%D0%B8-1/%D0%91%D0%B5%D0%B7%D0%BE%D0%B3%D0%BB%D0%B5%D0%B4%D0%B0%D0%BB%D0%BD%D0%B8-%D1%84%D0%BE%D1%82%D0%BE%D0%B0%D0%BF%D0%B0%D1%80%D0%B0%D1%82%D0%B8-3' # Replace with the actual URL
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    products = soup.find_all('h1', class_='title')
    product_links = []
    for product in products:
        link = product.find("a")["href"]
        product_links.append(link)
    # Read the previously saved product links from the text file (if it exists)
    previous_product_links = []
    file_name = "productsFromPhotoPavilion.txt"
    if not product_links:
        message = "No product links found on the webpage."
    else:
        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as file:
                previous_product_links = [line.strip() for line in file.readlines()]
        # Compare the current list of product links with the previously saved list
        new_product_links = list(set(product_links) - set(previous_product_links))
        if new_product_links:
            # If there are any new links, write the updated list to the text file
            with open(file_name, "w", encoding="utf-8") as file:
                for link in product_links:
                    file.write(f"{link}\n")
            message = "New product links found:\n\n" + "\n".join(new_product_links)
        else:
            message = "No new product links found in PhotoPavilion."
    # Send a message on Telegram with the product links
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    bot = Bot(bot_token)
    await bot.send_message(chat_id=chat_id, text=message)
    if new_product_links:
        await bot.send_message(chat_id=chat_id, text="Here are the new product links:")
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                await bot.send_message(chat_id=chat_id, text=line.strip())
asyncio.run(main())