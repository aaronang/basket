from collections import Counter, OrderedDict, defaultdict
from datetime import datetime
from typing import Dict, List, Tuple

from inflection import pluralize

from basket.helpers import pairs
from basket.ride import Count, Item, Ride

StartTime = datetime
EndTime = datetime
ItemCount = Tuple[Item, Count]
ItemCounts = List[ItemCount]
ItemCountsPerTime = Dict[datetime, Dict[Item, Count]]


class ItemCounter:
    _rides: List[Ride]

    def __init__(self) -> None:
        self._rides = []

    @property
    def rides(self) -> List[Ride]:
        return self._rides

    def process_ride(self, ride: Ride) -> None:
        self._rides.append(ride)

    def print_items_per_interval(self) -> None:
        for start_time, end_time, items in self._items_per_interval():
            items = self._format_items(items)
            print('{} - {} -> {}'.format(start_time, end_time, items))

    def _items_per_interval(self) -> List[Tuple[StartTime, EndTime, ItemCounts]]:
        items_per_start_time, items_per_end_time = self._items_per_start_and_end_time()
        timestamps = self._sorted_timestamps(items_per_start_time, items_per_end_time)
        basket = Counter()
        for start_time, end_time in pairs(timestamps):
            start_items = items_per_start_time.pop(start_time, Counter())
            end_items = items_per_end_time.pop(start_time, Counter())
            basket = basket + start_items - end_items
            yield (start_time, end_time, sorted(basket.items()))

    def _items_per_start_and_end_time(self) -> Tuple[ItemCountsPerTime, ItemCountsPerTime]:
        items_per_start_time = defaultdict(Counter)
        items_per_end_time = defaultdict(Counter)
        for start_time, end_time, items in self.rides:
            items_per_start_time[start_time] = items_per_start_time[start_time] + Counter(items)
            items_per_end_time[end_time] = items_per_end_time[end_time] + Counter(items)
        items_per_start_time = OrderedDict(sorted(items_per_start_time.items()))
        items_per_end_time = OrderedDict(sorted(items_per_end_time.items()))
        return items_per_start_time, items_per_end_time

    def _sorted_timestamps(self, start_times, end_times):
        return sorted({**start_times, **end_times}.keys())

    def _format_items(self, items):
        items = [self._format_item_count(item, count) for item, count in items]
        return ",".join(items)

    def _format_item_count(self, item: str, count: int) -> str:
        if count > 1:
            return "{} {}".format(count, pluralize(item))
        return "{} {}".format(count, item)
