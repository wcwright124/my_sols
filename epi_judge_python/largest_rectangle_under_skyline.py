from test_framework import generic_test


def calculate_largest_rectangle(heights):
    # TODO - you fill in here.
    max_area = 0
    stack = []
    for i, h in enumerate(heights + [0]):
        while stack and stack[-1][0] >= h:
            height, _ = stack.pop()
            width = i - stack[-1][1] - 1 if stack else i
            area = height * width
            max_area = max(max_area, area)
        stack.append((h, i))
    return max_area


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("largest_rectangle_under_skyline.py",
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
