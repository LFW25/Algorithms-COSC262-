"""A broken implementation of a recursive search for the optimal path through
   a grid of weights.
   Richard Lobb, January 2019.
"""
INFINITY = float('inf')  # Same as math.inf

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid

def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])

    def cell_cost(row, col):

        """The cost of getting to a given cell in the current grid."""
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            return INFINITY  # Off-grid cells are treated as infinities
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

def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))


from collections import defaultdict

def coins_reqd(value, coinage):
    """A version that doesn't use a list comprehension"""
    coin_chosen = [0] * (value + 1)
    numCoins = [0] * (value + 1)
    for amt in range(1, value + 1):
        minimum = None
        for c in coinage:
            if amt >= c:
                coin_count = numCoins[amt - c]  # Num coins required to solve for amt - c
                if minimum is None or coin_count < minimum:
                    minimum = coin_count
                    coin_chosen[amt] = c
        numCoins[amt] = 1 + minimum
    
    coins = defaultdict(int)
    i = len(coin_chosen) - 1
    while i != 0:
        coins[coin_chosen[i]] += 1
        i -= coin_chosen[i]
    
    coins_used = []
    for items in coins.items():
        coins_used.append(items)
    
    coins_used.sort(key=lambda x: x[0], reverse=True)
    return coin_chosen


print(coins_reqd(32, [1, 10, 25]))

# [(10, 3), (1, 2)]




import sys
sys.setrecursionlimit(2000)

class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"

cache = {}

def max_value(items, capacity):
    n = len(items)
    if n == 0:
        return 0
        
    elif (n, capacity) in cache:
        return cache[(n, capacity)]

    else:
        if items[-1].weight > capacity:
            cache[(n, capacity)] = max_value(items[:-1], capacity)

        else:
            val_1 = max_value(items[:-1], capacity)
            val_2 = max_value(items[:-1], capacity - items[-1].weight) + items[-1].value
            cache[(n, capacity)] = max(val_1, val_2)

    return cache[(n, capacity)]

cache = {}  

# The example from the lecture notes
items = [
    Item(45, 3),
    Item(45, 3),
    Item(80, 4),
    Item(80, 5),
    Item(100, 8)]
print(max_value(items, 10))
"""
170
"""

                              

# A large problem (500 items)
import random
random.seed(12345)  # So everyone gets the same
items = [Item(random.randint(1, 100), random.randint(1, 100)) for i in range(500)]
print(max_value(items, 500))

# 4422
