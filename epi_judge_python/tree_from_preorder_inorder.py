from test_framework import generic_test

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def binary_tree_from_preorder_inorder2(preorder, inorder):
    # TODO - you fill in here.
    def helper(preorder, inorder):
        if (not preorder) or (not inorder):
            return None
        root_val = preorder[0]
        root_idx = inorder.index(root_val)
        left_pre = preorder[1:root_idx+1]
        right_pre = preorder[root_idx+1:]
        left_in = inorder[:root_idx]
        right_in = inorder[root_idx+1:]
        root = BinaryTreeNode(root_val)
        root.left = helper(left_pre, left_in)
        root.right = helper(right_pre, right_in)
        return root
    return helper(preorder, inorder)

def binary_tree_from_preorder_inorder(preorder, inorder):
    def helper(pre_start, pre_end, in_start, in_end):
        if pre_end <= pre_start or in_end <= in_start:
            return None
        root_val = preorder[pre_start]
        root_idx = inorder_idx[root_val]
        left_pre_end = right_pre_start = pre_start + 1 + root_idx - in_start
        root = BinaryTreeNode(root_val)
        root.left = helper(pre_start + 1, left_pre_end, in_start, root_idx)
        root.right = helper(right_pre_start, pre_end, root_idx + 1, in_end)
        return root
    inorder_idx = {val: i for i, val in enumerate(inorder)}
    return helper(0, len(preorder), 0, len(inorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
