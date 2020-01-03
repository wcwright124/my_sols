from test_framework import generic_test


def can_reach_end(A):
    # TODO - you fill in here.
    if len(A) <= 1:
        return True
    moves_remaining = A[0]
    for i in range(len(A)):
        if moves_remaining == 0:
            return False
        moves_remaining -= 1
        moves_remaining = max(moves_remaining, A[i])
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
