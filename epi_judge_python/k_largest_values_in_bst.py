import heapq

from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    def helper(node):
        if node and len(res) < k:
            helper(node.right)
            if len(res) < k:
                res.append(node.data)
                helper(node.left)
        return
    # TODO - you fill in here.
    res = []
    helper(tree)
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
