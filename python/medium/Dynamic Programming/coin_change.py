import math


def coin_change(coins: list[int], amount: int) -> int:
    """
    Return the fewest number of coins needed to make the given amount.
    """

    #Sort the list.
    coins.sort()

    #Initialize the dp table.
    #Either math.inf or float('inf')
    dp = [math.inf] * (amount + 1)

    dp[0] = 0


    for i in range(1, amount + 1):
        #Try all coins.
        for coin in coins:
            if (i - coin) >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return int(dp[amount])


if __name__ == '__main__':
    print(coin_change([1, 2, 5], 11))
