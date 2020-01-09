from test_framework import generic_test


def look_and_say(n: int) -> str:
    # TODO - you fill in here.
    def get_next(curr):
        res = []
        left, right = 0, 0
        while right < len(curr):
            while right < len(curr) and curr[left] == curr[right]:
                right += 1
            res.append(str(right-left))
            res.append(str(curr[left]))
            left = right
        return ''.join(res)
    if n == 1:
        return '1'
    res = '1'
    for _ in range(1, n):
        res = get_next(res)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
