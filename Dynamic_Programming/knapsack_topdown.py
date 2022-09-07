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
    """
    Calculates the maximum value of items with a limited capacity
    using top-down recursion and memoisation
    """
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