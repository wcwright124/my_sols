import collections
import string

from test_framework import generic_test

# Uses BFS to find the least steps of transformation.
def transform_string(D, s, t):
    # TODO - you fill in here.
    queue = collections.deque([(s, 0)])
    D.remove(s)
    while queue:
        x, d = queue.popleft()
        if x == t:
            return d
        for i in range(len(x)):
            for c in string.ascii_lowercase:
                temp = x[:i] + c + x[i+1:]
                if temp in D:
                    D.remove(temp)
                    queue.append((temp, d + 1))
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
