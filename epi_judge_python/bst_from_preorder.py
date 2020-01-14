from test_framework import generic_test

class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def rebuild_bst_from_preorder(preorder_sequence): # O(n) time | O(n) space [for result, O(1) additional)]
    def helper(_min, _max):
        if root_idx[0] == len(preorder_sequence):
            return None
        root = preorder_sequence[root_idx[0]]
        if not (_min <= preorder_sequence[root_idx[0]] <= _max):
            return None
        root_idx[0] += 1
        left_sub = helper(_min, root)
        right_sub = helper(root, _max)
        return BSTNode(root, left_sub, right_sub)
    root_idx = [0]
    return helper(float('-inf'), float('inf'))


def rebuild_bst_from_preorder2(preorder_sequence):
    # TODO - you fill in here.
    def helper(lo, hi):
        if hi < lo:
            return None
        root = BSTNode(preorder_sequence[lo])
        new_idx = lo + 1
        while new_idx <= hi and preorder_sequence[new_idx] < preorder_sequence[lo]:
            new_idx += 1
        root.left = helper(lo+1, new_idx-1)
        root.right = helper(new_idx, hi)
        return root
    start, end = 0, len(preorder_sequence) - 1
    return helper(start, end)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
