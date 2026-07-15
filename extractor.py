import requests
from bs4 import BeautifulSoup
import pandas as pd
#Get the URL
print("Type the URL you would like to scrape: ")
url = input()
r = requests.get(url)
#Check if I can scrape
print(r.status_code)
#Grab the full HTML
soup = BeautifulSoup(r.content, "html.parser")
#Grab the parts you want of the HTML

scraped_item = soup.find_all("article", {"class": "product_pod"})

all_products = []

for product in scraped_item:
    title = product.find("h3").find("a")["title"]
    price = product.find("p", {"class": "price_color"}).text
    availability = product.find("p", {"class": "instock availability"}).text.strip()
    rating = product.find("p", {"class": "star-rating"})["class"][1]
    product_url = product.find("h3").find("a")["href"]

    useful_info = {
        "Title": title,
        "Price": price,
        "Availability": availability,
        "Rating": rating,
        "Product URL": product_url
    }

    all_products.append(useful_info)

#How many of that thing was found
print("Found " + str(len(scraped_item)) + " of the product you were searching for")

#Convert to Dataframe for exporting
df = pd.DataFrame(all_products)
print("Scraping completed")
print("How would you like your files? \n1. Excel (xlsx) \n2. CSV")
answer = input()
while answer != "1" and answer != "2":
    print("Please enter either 1 or 2")
    answer = input()
if answer == "1":
    df.to_excel("output/scraped_data.xlsx", index=False)
elif answer == "2":
    df.to_csv("output/scraped_data.csv", index=False)
