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

def max_value(items, capacity):

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


# # The example in the lecture notes
# items = [Item(45, 3),
#          Item(45, 3),
#          Item(80, 4),
#          Item(80, 5),
#          Item(100, 8)]
# print(max_value(items, 10))

# # 170
# # [Item(80, 4), Item(45, 3), Item(45, 3)]

cache = {}

def lcs(s1, s2):
    if s1 == '' or s2 == '':
        return ''

    elif (s1, s2) in cache:
        return cache[(s1, s2)]

    else:
        if s1[-1] == s2[-1]:
            cache[(s1, s2)] = lcs(s1[:-1], s2[:-1]) + s1[-1]

        else:
            sol_1 = lcs(s1[:-1], s2)
            sol_2 = lcs(s1, s2[:-1])

            if len(sol_1) > len(sol_2):
                cache[(s1, s2)] = sol_1

            else:
                cache[(s1, s2)] = sol_2
        return cache[(s1, s2)]

cache = {}
# # A simple test that should run without caching
# s1 = "abcde"
# s2 = "qbxxd"
# lcs = lcs(s1, s2)
# print(lcs)
# bd

s1 = "Look at me, I can fly!"
s2 = "Look at that, it's a fly"
print(lcs(s1, s2))
# Look at ,  a fly

s1 = "abcdefghijklmnopqrstuvwxyz"
s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
print(lcs(s1, s2))
# 

s1 = "balderdash!"
s2 = "balderdash!"
print(lcs(s1, s2))
# balderdash!