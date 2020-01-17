import collections

from test_framework import generic_test


def fill_surrounded_regions(board):
    def bfs(i, j):
        queue = collections.deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            if board[x][y] == 'W':
                board[x][y] = 'x'
            neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for a, b in neighbors:
                if 0 <= a < n and 0 <= b < m and board[a][b] == 'W':
                    queue.append((a, b))
    
    # TODO - you fill in here.
    n, m = len(board), len(board[0])
    for i in range(n):
        if board[i][0] == 'W':
            bfs(i, 0)
        if board[i][m - 1] == 'W':
            bfs(i, m - 1)
    for j in range(1, m - 1):
        if board[0][j] == 'W':
            bfs(0, j)
        if board[n - 1][j] == 'W':
            bfs(n - 1, j)

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'x':
                board[i][j] = 'W'
            else:
                board[i][j] = 'B'
    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
