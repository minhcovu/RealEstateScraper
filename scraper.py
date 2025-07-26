import requests
import csv
import BeautifulSoup

url = "https://www.homely.com.au/for-sale/adelaide-sa-5000/real-estate"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

listings = soup.select('a[aria-label][href^="/homes/"]')

data = []

# Extract address from listings
for listing in listings:
    listing_dict = {}
    listing_dict["address"] = listing.get("aria-label", "").strip()
    data.append(listing_dict)

# Write to a CSV file
with open("exports/homely_listings.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
