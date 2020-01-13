from test_framework import generic_test


def test_collatz_conjecture(n):
    # TODO - you fill in here.
    valid_nums = set([1,2])
    for i in range(3, n+1):
        x = i
        curr_seq = set()
        while x >= i:
            if x in valid_nums:
                break
            if x in curr_seq:
                return False
            curr_seq.add(x)
            if x % 2 == 0:
                x //= 2
            else:
                x = 3 * x + 1
        valid_nums.update(curr_seq)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("collatz_checker.py",
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
