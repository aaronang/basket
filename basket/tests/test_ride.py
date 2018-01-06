from datetime import datetime

from basket.ride import Ride


def test_ride() -> None:
    ride = Ride(
        start_time=datetime(2017, 1, 5, 7),
        end_time=datetime(2017, 1, 5, 7, 30),
        items={
            'apple': 2,
            'brownie': 1,
        })

    assert ride.items['apple'] == 2
    assert ride.items['brownie'] == 1
