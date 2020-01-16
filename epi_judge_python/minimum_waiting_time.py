from test_framework import generic_test


def minimum_total_waiting_time(service_times):
    # TODO - you fill in here.
    service_times.sort()
    total = 0
    sum_so_far = 0
    for time in service_times:
        total += sum_so_far
        sum_so_far += time
    return total


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_waiting_time.py",
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
