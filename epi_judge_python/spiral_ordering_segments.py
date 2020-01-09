from test_framework import generic_test

def update(bounds, dir):
    RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
    x, y = bounds[dir]
    if dir == RIGHT:
        bounds[RIGHT] = (x+1, y-1)
    elif dir == DOWN:
        bounds[DOWN] = (x-1, y-1)
    elif dir == LEFT:
        bounds[LEFT] = (x-1, y+1)
    elif dir == UP:
        bounds[UP] = (x+1, y+1)
    return bounds

def matrix_in_spiral_order(square_matrix):
    # TODO - you fill in here.
    n = len(square_matrix)
    # RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
    bounds = [(0, n-1), (n-1, n-1), (n-1, 0), (1,0)]
    direction_vects = [(0,1), (1,0), (0,-1), (-1, 0)]
    dir = 0
    num_elts = n ** 2
    res = []
    i, j = 0, 0
    while len(res) < num_elts:
        res.append(square_matrix[i][j])
        if (i, j) == bounds[dir]:
            bounds = update(bounds, dir)
            dir = (dir + 1) % 4
        dx, dy = direction_vects[dir]
        i, j = i + dx, j + dy
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
