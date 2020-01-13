from test_framework import generic_test

def find_first_greater_than_k(tree, k): # iterative solution
    res = None
    while tree:
        if tree.data <= k:
            tree = tree.right
        else:
            res = tree
            tree = tree.left
    return res


def find_first_greater_than_k2(tree, k): # recursive
    def helper(node, candidate=None):
        if node:
            if node.data <= k:
                return helper(node.right, candidate)
            else:
                candidate = node
                return helper(node.left, candidate)
        return candidate
    # TODO - you fill in here.
    candidate = helper(tree)
    return candidate


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
