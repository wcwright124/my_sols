import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def exterior_binary_tree(tree): # cleaner than first sol'n
    def is_leaf(root):
        return (not root.left) and (not root.right)
    
    def add_left(root):
        if (not root) or is_leaf(root):
            return
        res.append(root)
        if root.left:
            add_left(root.left)
        else:
            add_left(root.right)

    def add_leaves(root):
        if not root:
            return
        if is_leaf(root):
            res.append(root)
        add_leaves(root.left)
        add_leaves(root.right)

    def add_right(root):
        if (not root) or is_leaf(root):
            return
        if root.right:
            add_right(root.right)
        else:
            add_right(root.left)
        res.append(root)
        
    res = []
    if not tree:
        return res
    res.append(tree)
    add_left(tree.left)
    add_leaves(tree.left)
    add_leaves(tree.right)
    add_right(tree.right)
    return res

def exterior_binary_tree2(tree):
    def get_left_nodes(root):
        left_nodes = [root]
        root = root.left
        while root:
            left_nodes.append(root)
            if root.left:
                root = root.left
            else:
                root = root.right
        return left_nodes
    
    def get_children(root, res =[]):
        if not root:
            return res
        if (not root.left) and (not root.right):
            res.append(root)
        get_children(root.left, res)
        get_children(root.right, res)
        return res
    
    def get_right_nodes(root):
        right_nodes = []
        root = root.right # skip root
        while root:
            right_nodes.append(root)
            if root.right:
                root = root.right
            else:
                root = root.left
        return right_nodes
    # TODO - you fill in here.
    if not tree:
        return []
    left_nodes = get_left_nodes(tree)
    children = get_children(tree)
    right_nodes = get_right_nodes(tree)
    if children and right_nodes:
        right_nodes.pop()
    right_nodes.reverse()
    while left_nodes and children and left_nodes[-1] is children[0]:
        left_nodes.pop()
    res = left_nodes + children
    while right_nodes and res and res[-1] is right_nodes[0]:
        res.pop()
    res += right_nodes
    return res


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_exterior.py", 'tree_exterior.tsv',
                                       create_output_list_wrapper))
