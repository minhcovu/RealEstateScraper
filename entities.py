from dataclasses import dataclass
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