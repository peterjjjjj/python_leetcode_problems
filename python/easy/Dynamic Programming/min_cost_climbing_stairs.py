import math

def min_cost_climbing_stairs(cost: list[int]) -> int:
    """
    You are given an array cost of stairs.
    Return the min cost to reach the top.
    """

    #Initialize dp table.
    dp = [math.inf] * (len(cost) + 1)
    dp[0] = 0
    dp[1] = 0


    for i in range(2, len(dp)):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

    return dp[-1]

if __name__ == '__main__':
    print(min_cost_climbing_stairs([1,100,1,1,1,100,1,1,100,1]))

