import requests
import csv
from bs4 import BeautifulSoup

from listing_parser import parse_prices
from entities import Listing

class Scraper:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()

    def fetch_page(self, url):
        response = self.session.get(url)
        response.raise_for_status()
        return response.text
    
    def parse_listings(self, html) -> list[Listing]:
        soup = BeautifulSoup(html, "html.parser")

        listings_html = soup.select('a[aria-label][href^="/homes/"]')

        listings = []

        for listing in listings_html:

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
                "address": address,
                "min_price": price_range.min_price,
                "max_price": price_range.max_price,
                "beds": beds,
                "baths": baths,
                "cars": cars,
                "listing_type": property_type,
                "days_listed": days_listed,
            }

            listings.append(listing_dict)

        return listings


    def scrape(self) -> list[Listing]:
        html = self.fetch_page(self.url)
        listings = self.parse_listings(html)

        return listings

    def export_to_csv(self, path, listings: list[Listing]):
        with open(path, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=listings[0].keys())
            writer.writeheader()
            writer.writerows(listings)
