from test_framework import generic_test


def is_balanced_binary_tree(tree):
    # TODO - you fill in here.
    def helper(node, height):
        if not node:
            return True, height
        else:
            is_left_balanced, left_height = helper(node.left, height+1)
            is_right_balanced, right_height = helper(node.right, height+1)
            is_balanced = is_left_balanced and is_right_balanced and abs(left_height - right_height) <= 1
            new_height = max(left_height, right_height)
            return is_balanced, new_height
    is_balanced, _ = helper(tree, -1)
    return is_balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
