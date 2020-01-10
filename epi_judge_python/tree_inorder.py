from test_framework import generic_test

def inorder_traversal_recursive(tree):
    # TODO - you fill in here.
    def helper(node):
        if node:
            helper(node.left)
            res.append(node.data)
            helper(node.right)
    res = []
    helper(tree)
    return res

def inorder_traversal(tree):
    # TODO - you fill in here.
    res = []
    stack = [(tree, False)]
    while stack:
        node, traversed_left = stack.pop()
        if node:
            if traversed_left:
                res.append(node.data)
            else:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
