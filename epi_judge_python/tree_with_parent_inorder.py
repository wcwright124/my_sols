from test_framework import generic_test


def inorder_traversal2(tree):
    # TODO - you fill in here.
    res = []
    if not tree:
        return res
    node = tree
    while node.left:
        node = node.left
    res.append(node.data)
    while node:
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            res.append(node.data)
        else:
            while node.parent and (node.parent.right is node):
                node = node.parent
            node = node.parent
            if node:
                res.append(node.data)
    return res

def inorder_traversal(tree):
    prev = None
    res = []
    while tree:
        if prev is tree.parent:
            if tree.left:
                prev, tree = tree, tree.left
            else:
                res.append(tree.data)
                if tree.right:
                    prev, tree = tree, tree.right
                else:
                    prev, tree = tree, tree.parent
        elif prev is tree.left:
            res.append(tree.data)
            if tree.right:
                prev, tree = tree, tree.right
            else:
                prev, tree = tree, tree.parent
        elif prev is tree.right:
            prev, tree = tree, tree.parent
    return res


        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
