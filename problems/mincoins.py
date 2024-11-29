
def deduct_coins(val, coin_val):
    count = val // coin_val
    val -= (count*coin_val)
    return val, count

def min_coins(coins, val):
    if val == coins[-1]:
        return 1
    
    i = len(coins) - 1
    required = 0

    if val > coins[-1]:
        val, count = deduct_coins(val, coins[-1])
        required += count
    
    while val < coins[i] and i >= 0:
        i -= 1

        if val >= coins[i]:
            val, count = deduct_coins(val, coins[i])
            required += count
    return required



# coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

# print(min_coins(coins, 3063))

# print(min_coins(coins, 3))

#############################################################

# minimum coins with variable coins system


def min_coins_var(coins, val):
    coins.sort(reverse=True)  # O(nlogn)
    required = 0
    if val > coins[0]:
        val, required = deduct_coins(val, coins[0])

    for coin_val in coins:
        if val >= coin_val:
            val, count = deduct_coins(val, coin_val)
            required += count
    
    return required if not val else -1

# coins = [25, 10, 5]

sum = 30

print(min_coins_var([25, 10, 5], 30))

print(min_coins_var([4, 6, 2], 5))


# print(min_coins(coins, sum))