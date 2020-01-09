from test_framework import generic_test


def generate_pascal_triangle(n): # O(n ** 2) time and space 
    # TODO - you fill in here.
    if n == 0:
        return []
    res = [[1]]
    if n == 1:
        return res
    res.append([1, 1])
    if n == 2:
        return res
    for _ in range(2, n):
        temp = [1]
        for i in range(1, len(res[-1])):
            temp.append(res[-1][i] + res[-1][i-1])
        temp.append(1)
        res.append(temp)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pascal_triangle.py",
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
