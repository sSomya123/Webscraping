import requests
import os
from bs4 import BeautifulSoup

url ="https://www.w3schools.com/"

content = requests.get(url)

soup=BeautifulSoup(content.text,"html.parser")

if not os.path.exists("data"):
    os.makedirs("data")
    

with open("data/scraped_page.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())
#print(soup.prettify())

headings = soup.find_all(['h1', 'h2', 'h3'])
with open("data/scraped_headings.html", "w", encoding="utf-8") as file:
    for heading in headings:
        file.write(heading.get_text() + "\n")

links = soup.find_all('a', href=True)
with open("data/scraped_links.html", "w", encoding="utf-8") as file:
    for link in links:
        file.write(link.get_text() + "\n")

images = soup.find_all('img', src=True)
with open("data/scraped_imgs.html", "w", encoding="utf-8") as file:
    for img in images:
        file.write(img['src'])

print("Scraping complete. Check the 'data' folder for the HTML files.")
