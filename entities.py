from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from typing import Optional

@dataclass
class PriceRange():
    """Class to store min and max price range of a listing."""
    min_price: Optional[int]
    max_price: Optional[int]

    def formatted(self) -> str:
        if self.min_price is None or self.max_price is None:
            return "N/A"
        elif self.min_price == self.max_price:
            return f"${self.min_price}"
        else:
            return f"${self.min_price} - ${self.max_price}"
        
Base = declarative_base()

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, nullable=False)
    min_price = Column(Integer, nullable=True)
    max_price = Column(Integer, nullable=True)
    beds = Column(Integer, nullable=True)
    baths = Column(Integer, nullable=True)
    cars = Column(Integer, nullable=True)
    listing_type = Column(String, nullable=False)
    days_listed = Column(String, nullable=False)

    def to_dict(self):
        return {
            "address": self.address,
            "min_price": self.min_price,
            "max_price": self.max_price,
            "beds": self.beds,
            "baths": self.baths,
            "cars": self.cars,
            "listing_type": self.listing_type,
            "days_listed": self.days_listed,
            "id": self.id,
        }
