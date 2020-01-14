import collections

from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree, interval):
    # TODO - you fill in here.
    def helper(root):
        if not root:
            return
        if interval.left <= root.data <= interval.right:
            helper(root.left)
            res.append(root.data)
            helper(root.right)
        elif root.data > interval.right:
            helper(root.left)
        else:
            helper(root.right)
    res = []
    helper(tree)
    return res


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("range_lookup_in_bst.py",
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
