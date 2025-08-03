from real_estate_scraper.listing_parser import parse_prices

def test_output_format():

    examples = [
        "$650,000 ~ $670,000",
        "$650,000 - $670,000",
        "$780,000",
        "$1.3m-$1.4m",
        "Best Offer by 18 August | $1,400,000 - $1,540,000",
        "$1.3m-$1.4m|Best Offers By Tues 05/08/25",
        "New"
    ]

    expected = [
        "$650000 - $670000",
        "$650000 - $670000",
        "$780000",
        "$1300000 - $1400000",
        "$1400000 - $1540000",
        "$1300000 - $1400000",
        "N/A"
    ]

    result = [parse_prices(p).formatted() for p in examples]

    assert result == expected
