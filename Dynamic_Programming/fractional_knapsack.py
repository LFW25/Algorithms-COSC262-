def fractional_knapsack(capacity, items):
    """
    Returns the maximum value of items in a limited capacity knapsack
    when you're allowed parts of items
    """
    items.sort(key = lambda x: x[1]/x[2], reverse = True)
    current_weight = 0
    value = 0

    for (item, it_value, it_weight) in items:
        weight_dif = capacity - current_weight
        if weight_dif > 0:
            if weight_dif >= it_weight:
                value += it_value
                current_weight += it_weight
            else:
                ratio = weight_dif/it_weight
                value += it_value * ratio
                current_weight += it_weight * ratio
    
    return value