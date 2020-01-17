import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self):
        self.d = -1
        self.edges = []

# from book, compute distance from starting node
# if two equidistant nodes share an edge, return False
# if you finish traversal, you can return True
# NB: modding by 2 produces the 2-coloring we did here

def is_any_placement_feasible(graph): # use bfs to produce a 2-coloring
    def bfs(node):
        queue = collections.deque([node])
        d = 0
        while queue:
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                curr_node.d = d
                for n in curr_node.edges:
                    if n.d == -1:
                        queue.append(n)
                    if n.d == d:
                        return False
            d = (not d)
        return True
    # TODO - you fill in here.
    for node in graph:
        if node.d == -1 and not bfs(node):
                return False
    return True


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_circuit_wirable.py",
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
