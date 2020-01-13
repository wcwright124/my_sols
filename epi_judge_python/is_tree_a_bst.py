from test_framework import generic_test


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    # TODO - you fill in here.
    if not tree:
        return True
    elif low_range <= tree.data <= high_range:
        is_left_bst = is_binary_tree_bst(tree.left, low_range, tree.data)
        is_right_bst = is_binary_tree_bst(tree.right, tree.data, high_range)
        return is_left_bst and is_right_bst
    else:
        return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
