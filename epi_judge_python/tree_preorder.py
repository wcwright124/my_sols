from test_framework import generic_test


def preorder_traversal_recursive(tree):
    # TODO - you fill in here.
    def helper(node):
        if node:
            res.append(node.data)
            helper(node.left)
            helper(node.right)
    res = []
    helper(tree)
    return res

def preorder_traversal(tree):
    res = []
    if not tree:
        return res
    stack = [tree]
    while stack:
        node = stack.pop()
        res.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))
