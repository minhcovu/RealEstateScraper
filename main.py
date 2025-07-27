from scraper import Scraper
from pprint import pprint

def main():
    scraper = Scraper("https://www.homely.com.au/for-sale/adelaide-sa-5000/real-estate")
    listings = scraper.scrape()

    pprint(listings)

    scraper.export_to_csv("exports/homely_listings.csv", listings)

if __name__ == "__main__":
    main()