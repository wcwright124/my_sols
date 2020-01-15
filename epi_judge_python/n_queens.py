from test_framework import generic_test


def n_queens(n):
    def helper(row):
        if row == n:
            res.append(partial[:])
            return
        else:
            invalid_positions = set()
            for pos_row, pos in enumerate(partial):
                invalid_positions.add(pos - (row - pos_row))
                invalid_positions.add(pos)
                invalid_positions.add(pos + (row - pos_row))
            for col in range(n):
                if col not in invalid_positions:
                    partial.append(col)
                    helper(row + 1)
                    partial.pop()
    # TODO - you fill in here.
    res = []
    partial = []
    helper(0)
    return res


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
