from bs4 import BeautifulSoup
import requests
import os
import asyncio
from telegram import Bot
from dotenv import load_dotenv
load_dotenv()

async def main():
    url = 'https://magazin.photosynthesis.bg/bg/939-bezogledalni-fotoaparati' # Replace with the actual URL
    base_url = 'https://magazin.photosynthesis.bg'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    products = soup.find_all('h3', itemprop='name')
    product_links = []
    for product in products:
        link = product.find("a")["href"]
        full_url = base_url + link
        product_links.append(full_url)
    # Read the previously saved product links from the text file (if it exists)
    previous_product_links = []
    file_name = "productsFromPhotoSynthesis.txt"
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
            message = "No new product links found in PhotoSynthesis."
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