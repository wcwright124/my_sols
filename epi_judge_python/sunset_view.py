from test_framework import generic_test


def examine_buildings_with_sunset(sequence):
    # NB it makes more sense to do this problem by
    # travesing the sequence in reverse order and 
    # keeping track of the current tallest building
    stack = []
    for i, height in enumerate(sequence):
        if not stack:
            stack.append((i, height))
        else:
            while stack and stack[-1][1] <= height:
                stack.pop()
            stack.append((i, height))
    return [s[0] for s in reversed(stack)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
