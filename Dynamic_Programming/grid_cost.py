def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])

    def cell_cost(row, col):

        """The cost of getting to a given cell in the current grid."""
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            return float('inf')  # Off-grid cells are treated as infinities
        elif row == 0:
            return grid[row][col]
        else:
            if col == 0:
                grid[row][col] += min([grid[row-1][col+k] for k in [0, 1]])
            elif col == n_cols-1:
                grid[row][col] += min([grid[row-1][col+k] for k in range(-1, 1)])
            else:
                grid[row][col] += min([grid[row-1][col+k] for k in range(-1, 2)])
            return grid[row][col]    

    for row in range(1, n_rows):
        for col in range(n_cols):
            grid[row][col] = cell_cost(row, col)
    
    best = min([grid[n_rows-1][col] for col in range(n_cols)])
    return best