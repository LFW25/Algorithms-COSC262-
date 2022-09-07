from collections import defaultdict

def change_greedy(amount, coinage):
    """
    Given an amount, computes the change coinage using a greedy algorithm
    """
    coin_count = defaultdict(int)

    while amount > 0 and len(coinage) > 0:

        highest_coin = max(coinage)
        if amount - highest_coin >= 0:
            coin_count[highest_coin] += 1
            amount -= highest_coin
        else:
            coinage.remove(highest_coin)
    if amount > 0:
        return None
    else:
        counter = []
        for key in coin_count:
            counter.append((coin_count[key], key))
        return counter 