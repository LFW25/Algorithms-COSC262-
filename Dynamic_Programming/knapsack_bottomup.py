class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"

def max_value(items, capacity):
    """
    Calculates the maximum value of items with a limited capacity
    using bottom_up iteration
    """
    value_table = [[0 for i in range(capacity+1)] for i in range(len(items) + 1)]

    for i in range(len(items) + 1):

        for j in range(capacity + 1):

            if i == 0 or j == 0:
                value_table[i][j] = 0

            elif items[i-1].weight <= j:
                value_table[i][j] = max(items[i-1].value + value_table[i-1][j - items[i-1].weight], value_table[i-1][j])
                
            else:
                value_table[i][j] = value_table[i-1][j]
    
    result = value_table[-1][-1]
    cap = capacity
    n = len(items)
    items_used = []
    for i in range(n, 0, -1):
        if result <= 0:
            break
        if result == value_table[i - 1][cap]:
            continue
        else:
            items_used.append(items[i - 1])
            result = result - items[i-1].value
            cap = cap - items[i-1].weight

    return value_table[-1][capacity], items_used