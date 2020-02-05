from test_framework import generic_test


def find_element_appears_once(A):
    def handle_neg(n):
        return n if n < 2 ** 31 else n - 2 ** 32
    # TODO - you fill in here.
    bit_counts = [0] * 32
    for a in A:
        for i in range(32):
            bit_counts[i] += (a & 1)
            a >>= 1
    res = sum(1 << i for i, b in enumerate(bit_counts) if b % 3)
    return handle_neg(res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("element_appearing_once.py",
                                       'element_appearing_once.tsv',
                                       find_element_appears_once))
