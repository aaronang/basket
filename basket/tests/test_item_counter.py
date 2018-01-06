from datetime import datetime
from typing import List
from collections import OrderedDict

import pytest

from basket.item_counter import ItemCounter
from basket.ride import Ride


@pytest.fixture
def item_counter() -> ItemCounter:
    return ItemCounter()


@pytest.fixture
def rides() -> List[Ride]:
    return [
        Ride(
            start_time=datetime(2018, 1, 1, 7),
            end_time=datetime(2018, 1, 1, 7, 30),
            items={
                'apple': 2,
                'brownie': 1,
            }),
        Ride(
            start_time=datetime(2018, 1, 1, 7, 10),
            end_time=datetime(2018, 1, 1, 8),
            items={
                'apple': 1,
                'carrot': 3,
            }),
        Ride(
            start_time=datetime(2018, 1, 1, 7, 20),
            end_time=datetime(2018, 1, 1, 7, 45),
            items={
                'apple': 1,
                'brownie': 2,
                'diamond': 4,
            })
    ]


def populate_item_counter(item_counter: ItemCounter, rides: List[Ride]) -> None:
    for i, ride in enumerate(rides):
        item_counter.process_ride(ride)


def test_item_counter(item_counter: ItemCounter) -> None:
    assert len(item_counter.rides) == 0


def test_process_ride(item_counter: ItemCounter, rides: List[Ride]) -> None:
    for i, ride in enumerate(rides):
        item_counter.process_ride(ride)
        assert len(item_counter.rides) == i + 1


def test_items_per_interval(item_counter: ItemCounter, rides: List[Ride]) -> None:
    populate_item_counter(item_counter, rides)

    # yapf: disable
    expected = [
        (datetime(2018, 1, 1, 7), datetime(2018, 1, 1, 7, 10), [('apple', 2), ('brownie', 1)]),
        (datetime(2018, 1, 1, 7, 10), datetime(2018, 1, 1, 7, 20), [('apple', 3), ('brownie', 1), ('carrot', 3)]),
        (datetime(2018, 1, 1, 7, 20), datetime(2018, 1, 1, 7, 30), [('apple', 4), ('brownie', 3), ('carrot', 3), ('diamond', 4)]),
        (datetime(2018, 1, 1, 7, 30), datetime(2018, 1, 1, 7, 45), [('apple', 2), ('brownie', 2), ('carrot', 3), ('diamond', 4)]),
        (datetime(2018, 1, 1, 7, 45), datetime(2018, 1, 1, 8), [('apple', 1), ('carrot', 3)]),
    ]
    # yapf: enable
    assert item_counter.items_per_interval() == expected


def test_print_items_per_interval(item_counter: ItemCounter, rides: List[Ride]) -> None:
    populate_item_counter(item_counter, rides)
    item_counter.print_items_per_interval()
