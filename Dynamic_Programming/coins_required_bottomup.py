from collections import defaultdict

def coins_reqd(value, coinage):
    """The function returns the minimum number of coins required
    to make up the value as a list of tuples of the form
    (denomination, num_coins)
    where num_coins in the number of coins of the given denomination.
    The list includes only cases where num_coins is greater than zero.
    The list is in decreasing order of denomination."""
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