from test_framework import generic_test


def is_symmetric(tree):
    # TODO - you fill in here.
    def helper(root1, root2):
        if (not root1) and (not root2):
            return True
        elif root1 and root2:
            return root1.data == root2.data and helper(root1.left, root2.right) and helper(root1.right, root2.left)
        else:
            return False
    return (not tree) or helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
