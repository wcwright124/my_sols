from test_framework import generic_test, test_utils


def generate_power_set(S):
    # TODO - you fill in here.
    res = [[]]
    for s in S:
        for i in range(len(res)):
            res.append(res[i] + [s])
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
