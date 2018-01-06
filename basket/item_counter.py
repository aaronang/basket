from typing import List

from basket.ride import Ride


class ItemCounter:
    _rides: List[Ride]

    def __init__(self) -> None:
        self._rides = []

    @property
    def rides(self) -> List[Ride]:
        return self._rides

    def process_ride(self, ride: Ride) -> None:
        self._rides.append(ride)
