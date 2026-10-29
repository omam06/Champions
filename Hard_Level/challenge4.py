def minimum_coins(coins, amount):
    impossible = amount + 1
    minimum_coins_needed = [impossible] * (amount + 1)
    minimum_coins_needed[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                remaining_amount = value - coin 
                if minimum_coins_needed[remaining_amount] != impossible:
                    minimum_coins_needed[value] = min(minimum_coins_needed[value], 1 + minimum_coins_needed[remaining_amount])
    if minimum_coins_needed[amount] == impossible:
        return -1

    return minimum_coins_needed[amount]

print(minimum_coins([1, 2, 5], 11))
print(minimum_coins([2, 3, 4], 5))
print(minimum_coins([2, 4, 4], 5))