import collections

from test_framework import generic_test


def flip_color(x, y, image):
    def bfs(x, y):
        queue = collections.deque([(x, y)])
        while queue:
            i, j = queue.popleft()
            if image[i][j] == color:
                image[i][j] = not image[i][j]
                neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                for a, b in neighbors:
                    if 0 <= a < len(image) and 0 <= b < len(image[a]) and image[a][b] == color:
                        queue.append((a, b))
    
    def dfs(i, j):
        if not (0 <= i < len(image)) or not (0 <= j < len(image[i])):
            return
        if image[i][j] != color:
            return
        image[i][j] = not image[i][j]
        neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for a, b in neighbors:
            dfs(a, b)
    # TODO - you fill in here.
    color = image[x][y]
    bfs(x, y)
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
