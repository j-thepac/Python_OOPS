def greedy_coin_change(amount, coins):
    coins.sort(reverse=True)
    coins_used = []
    for coin in coins:
        while amount >= coin:
            coins_used.append(coin)
            amount -= coin
    return coins_used

amt = 63
coins = [1, 2, 5, 10, 20, 50]
print(greedy_coin_change(amt, coins))
