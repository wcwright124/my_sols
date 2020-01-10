from test_framework import generic_test


def has_path_sum(tree, remaining_weight):
    # TODO - you fill in here.
    if not tree:
        return False
    remaining_weight -= tree.data
    if (not tree.left) and (not tree.right): # leaf
        return remaining_weight == 0
    left = has_path_sum(tree.left, remaining_weight)
    right = has_path_sum(tree.right, remaining_weight)
    return left or right


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("path_sum.py", 'path_sum.tsv',
                                       has_path_sum))
