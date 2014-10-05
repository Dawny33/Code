def pickBest(coins,due):
     if due == 0: return []
     for c in coins:
        if c<= due: return [c] + pickBest(coins,due-c)

#Input the coins list in a reverse sorted order.
#Ex: sorted(coins, reverse = True)
