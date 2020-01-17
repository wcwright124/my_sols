from test_framework import generic_test


def get_max_trapped_water(heights):
    # TODO - you fill in here.
    left, right = 0, len(heights) - 1
    max_water = 0
    while left < right:
        current_water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, current_water)
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
    return max_water


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_trapped_water.py",
                                       "max_trapped_water.tsv",
                                       get_max_trapped_water))
