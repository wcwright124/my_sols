from test_framework import generic_test


# We use stack and previous node pointer to simulate postorder traversal.
def postorder_traversal_recursive(tree):
    # TODO - you fill in here.
    def helper(node):
        if node:
            helper(node.left)
            helper(node.right)
            res.append(node.data)
    res = []
    helper(tree)
    return res

def postorder_traversal(tree):
    res = []
    if not tree:
        return res
    stack = [(tree, False)]
    while stack:
        node, subtrees_traversed = stack.pop()
        if subtrees_traversed:
            res.append(node.data)
        else:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "tree_postorder.py", 'tree_postorder.tsv', postorder_traversal))
