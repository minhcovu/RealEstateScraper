from scraper import Scraper
from database import Database

from pprint import pprint

def main():
    scraper = Scraper("https://www.homely.com.au/for-sale/adelaide-sa-5000/real-estate")
    listings = scraper.scrape()

    scraper.export_to_csv("exports/homely_listings.csv", listings)

    database = Database()

    for listing in listings:
        database.insert_listing(listing)

if __name__ == "__main__":
    main()