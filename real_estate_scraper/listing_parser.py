from real_estate_scraper.entities import PriceRange
import re

def parse_prices(str_prices: str) -> PriceRange:

    # Clean up the price string
    unwanted = "-~, "
    cleaned_prices = str_prices
    for char in unwanted:
        cleaned_prices = cleaned_prices.replace(char,'')

    # Use Regex to find the price pair
    cleaned_prices = re.findall("\\$\\d+\\.\\d+m|\\$\\d+", cleaned_prices)

    cleaned_prices = [p.replace('$','') for p in cleaned_prices]

    # Convert "m" notation to $ value
    def convert(price):
        if price.endswith('m'):
            return int(float(price[:-1]) * 1000000)
        elif not price.isnumeric():
            return None
        else:
            return int(price)

    if not cleaned_prices:
        return PriceRange(None, None)

    price_min = convert(cleaned_prices[0])
    price_max = convert(cleaned_prices[1]) if len(cleaned_prices) > 1 else price_min

    return PriceRange(price_min, price_max)
