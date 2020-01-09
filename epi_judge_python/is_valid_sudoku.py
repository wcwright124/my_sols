from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def has_duplicates(vals):
    return len(vals) != len(set(vals))

def validate_row(grid, i):
    row = [g for g in grid[i] if g != 0]
    return not has_duplicates(row)

def validate_col(grid, j):
    col = [grid[i][j] for i in range(9) if grid[i][j] != 0]
    return not has_duplicates(col)

def validate_subgrid(grid, x, y):
    grid_vals = []
    for i in range(x, x+3):
        for j in range(y, y+3):
            if grid[i][j] != 0:
                grid_vals.append(grid[i][j])
    return not has_duplicates(grid_vals)

def is_valid_sudoku(partial_assignment):
    # TODO - you fill in here.
    for i in range(9):
        if not validate_row(partial_assignment, i):
            return False
        if not validate_col(partial_assignment, i):
            return False
    corners = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
    for i,j in corners:
        if not validate_subgrid(partial_assignment, i, j):
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
