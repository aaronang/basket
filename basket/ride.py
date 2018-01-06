from datetime import datetime
from typing import NamedTuple, Dict


class Ride(NamedTuple):
    start_time: datetime
    end_time: datetime
    items: Dict[str, int]
