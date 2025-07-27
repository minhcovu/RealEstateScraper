import requests
import csv
from bs4 import BeautifulSoup

from parser import parse_prices

url = "https://www.homely.com.au/for-sale/adelaide-sa-5000/real-estate"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

listings = soup.select('a[aria-label][href^="/homes/"]')

data = []

for listing in listings:

    # Extract address from listings
    address = listing.get("aria-label", "").strip()

    # Extract price (it's inside an h3 tag)
    price_tag = listing.select_one("h3")
    price_str = price_tag.get_text(strip=True) if price_tag else "N/A"
    
    price_range = parse_prices(price_str)

    # Extract bed, bath, car
    icons = listing.select("ul li")
    beds = icons[0].get_text(strip=True) if len(icons) > 0 else "0"
    baths = icons[1].get_text(strip=True) if len(icons) > 1 else "0"
    cars = icons[2].get_text(strip=True) if len(icons) > 2 else "0"

    # Extract property type and days
    tags = listing.select("div.truncate h4")
    property_type = tags[0].get_text(strip=True) if len(tags) > 0 else "N/A"
    days_listed = tags[1].get_text(strip=True) if len(tags) > 1 else "N/A"

    listing_dict = {
        "Address": address,
        "Min Price": price_range.min_price,
        "Max Price": price_range.max_price,
        "Beds": beds,
        "Baths": baths,
        "Cars": cars,
        "Type": property_type,
        "Days Listed": days_listed,
    }

    data.append(listing_dict)

    
# Write to a CSV file
with open("exports/homely_listings.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
