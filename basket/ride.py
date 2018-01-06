from datetime import datetime
from typing import NamedTuple, Dict

Item = str
Count = int


class Ride(NamedTuple):
    start_time: datetime
    end_time: datetime
    items: Dict[Item, Count]
