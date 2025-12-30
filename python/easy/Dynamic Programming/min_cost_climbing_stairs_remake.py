#2 solutions, bottom-up, topdown bottom

def dp(cost: list[int]) -> int:
    """
    TC: O(n)
    SC: O(n)
    """
    dp_table = [0] * (len(cost) + 1)

    for i in range(2, len(cost) + 1):
        dp_table[i] = min(dp_table[i - 1] + cost[i - 1], dp_table[i - 2] + cost[i - 2])

    return dp_table[-1]


def recursion(cost: list[int]) -> int:
    """
    TC: O(n)
    SC: O(n)
    """
    memo = {}

    def helper(n: int) -> int:
        if n == 1 or n == 0:
            return cost[n]

        if n in memo:
            return memo[n]

        #If n is the result stage with no cost, store the min of last 2 stages instead.
        if n < len(cost):
            memo[n] = cost[n] + min(helper(n - 1), helper(n - 2))
        else:
            memo[n] = min(helper(n - 1), helper(n - 2))

        #Return the last stage.
        return memo[n]

    return helper(len(cost) + 1)


if __name__ == '__main__':
    print(dp([10, 15, 20]))
    print(recursion([10, 15, 20]))