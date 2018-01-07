# Basket

Understanding the usefulness of bike baskets 🍋 🚲

## Quick Start

1. Install prerequisites:

   * [Python 3.6](https://www.python.org/downloads/release/python-364/)
   * [pip](https://pip.pypa.io/en/stable/installing/)
   * [Pipenv](https://docs.pipenv.org/)

1. Install `basket`:

   ```bash
   $ pip install -e git+https://github.com/aaronang/basket.git#egg=basket
   ```

1. Usage:

   ```python
   from basket import ItemCounter, Ride
   from datetime import datetime

   ride_1 = Ride(
       start_time=datetime(2018, 1, 1, 7),
       end_time=datetime(2018, 1, 1, 7, 30),
       items={
           'apple': 2,
           'brownie': 1,
       })

   ride_2 = Ride(
       start_time=datetime(2018, 1, 1, 7, 10),
       end_time=datetime(2018, 1, 1, 8),
       items={
           'apple': 1,
           'carrot': 3,
       })

   ride_3 = Ride(
       start_time=datetime(2018, 1, 1, 7, 20),
       end_time=datetime(2018, 1, 1, 7, 45),
       items={
           'apple': 1,
           'brownie': 2,
           'diamond': 4,
       })

   item_counter = ItemCounter()
   item_counter.process_ride(ride_1)
   item_counter.process_ride(ride_2)
   item_counter.process_ride(ride_3)
   item_counter.print_items_per_interval()
   ```

## Development Environment Setup

1. Install dependencies:

   ```bash
   $ pipenv install --dev
   ```

1. To run tests:

   ```bash
   $ pipenv run pytest
   ```

1. To run linter:
   ```bash
   $ pipenv run prospector
   ```
