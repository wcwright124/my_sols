import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20

CityAndRemainingGas = collections.namedtuple('CityAndRemainingGas', ('city', 'gas'))

# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
def find_ample_city(gallons, distances):
    # TODO - you fill in here.
    lowest_gas = 0
    remaining_gas = 0
    candidate = 0
    for i in range(1, len(gallons)):
        remaining_gas += gallons[i-1] - distances[i-1] / MPG
        if remaining_gas < lowest_gas:
            candidate = i 
            lowest_gas = remaining_gas
    return candidate


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    """tests = [
        [[20, 15, 15, 15, 35, 25, 30, 15, 65, 45, 10, 45, 25], [300, 400, 1000, 300, 300, 600, 400, 1100, 400, 1000, 200, 300, 300]]
    ]
    for t in tests:
        gallons, distances = t
        print(find_ample_city(gallons, distances))
    """
    exit(
        generic_test.generic_test_main("refueling_schedule.py",
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))#"""
