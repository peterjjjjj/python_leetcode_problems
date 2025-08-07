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
        #If we choose to jump from the previous step.
        if dp[i - 1] <= dp[i - 2]:
            dp[i] = dp[i - 1] + cost[i - 1]
        #Or the cost is lower 2 stairs behind.
        else:
            dp[i] = dp[i - 2] + cost[i - 2]

    return dp[-1]

if __name__ == '__main__':
    print(min_cost_climbing_stairs([10, 15, 25]))

