from datetime import datetime

import pytest

from basket.item_counter import ItemCounter
from basket.ride import Ride


@pytest.fixture
def item_counter():
    return ItemCounter()


def test_item_counter(item_counter):
    assert len(item_counter.rides) == 0


def test_process_ride(item_counter):
    ride_1 = Ride(
        start_time=datetime(2017, 1, 5, 7),
        end_time=datetime(2017, 1, 5, 7, 30),
        items={
            'apple': 2,
            'brownie': 1,
        })

    ride_2 = Ride(
        start_time=datetime(2017, 1, 5, 7, 10),
        end_time=datetime(2017, 1, 5, 8),
        items={
            'apple': 1,
            'carrot': 3,
        })

    item_counter.process_ride(ride_1)
    assert len(item_counter.rides) == 1

    item_counter.process_ride(ride_2)
    assert len(item_counter.rides) == 2
