from dataclasses import dataclass
from typing import Optional

@dataclass
class PriceRange():
    """Class to store min and max price range of a listing."""
    min_price: Optional[int]
    max_price: Optional[int]
