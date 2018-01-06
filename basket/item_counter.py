from datetime import datetime
from typing import List, Tuple, Dict

from itertools import tee
from basket.ride import Count, Item, Ride
from collections import defaultdict, Counter, OrderedDict

StartTime = datetime
EndTime = datetime
ItemCount = Tuple[Item, Count]
ItemCounts = List[ItemCount]
ItemCountsPerTime = Dict[datetime, Dict[Item, Count]]


def pairs(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


class ItemCounter:
    _rides: List[Ride]

    def __init__(self) -> None:
        self._rides = []

    @property
    def rides(self) -> List[Ride]:
        return self._rides

    def process_ride(self, ride: Ride) -> None:
        self._rides.append(ride)

    def items_per_interval(self) -> List[Tuple[StartTime, EndTime, ItemCounts]]:
        items_per_start_time, items_per_end_time = self._items_per_time()
        times = sorted({**items_per_start_time, **items_per_end_time}.keys())
        result = []
        basket = Counter()
        for start_time, end_time in pairs(times):
            start_items = items_per_start_time.pop(start_time, Counter())
            end_items = items_per_end_time.pop(start_time, Counter())
            basket = basket + start_items - end_items
            result.append((start_time, end_time, sorted(basket.items())))
        return result

    def _items_per_time(self) -> Tuple[ItemCountsPerTime, ItemCountsPerTime]:
        items_per_start_time = defaultdict(Counter)
        items_per_end_time = defaultdict(Counter)
        for ride in self.rides:
            start_time = ride.start_time
            end_time = ride.end_time
            items_per_start_time[start_time] = items_per_start_time[start_time] + Counter(ride.items)
            items_per_end_time[end_time] = items_per_end_time[end_time] + Counter(ride.items)
        items_per_start_time = OrderedDict(sorted(items_per_start_time.items()))
        items_per_end_time = OrderedDict(sorted(items_per_end_time.items()))
        return items_per_start_time, items_per_end_time

    def print_items_per_interval(self) -> None:
        for start_time, end_time, items in self.items_per_interval():
            items = [self._format_item_count(item, count) for item, count in items]
            print("{} - {} -> {}".format(start_time, end_time, ", ".join(items)))
