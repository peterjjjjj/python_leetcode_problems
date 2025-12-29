#dp, recursion,

def dp(n: int) -> int:
    """
    TC: O(n)
    SC: O(n)
    """
    if n == 1:
        return 1

    #The values for first 2 steps
    dp_table = [0] * (n + 1)
    dp_table[1] = 1
    dp_table[2] = 2

    #Start with i = 2 since first were satup
    for i in range(3, n + 1):
        dp_table[i] = dp_table[i - 1] + dp_table[i - 2]

    return dp_table[n]

def recursion(n: int) -> int:
    """
    TC: O(n)
    SC: O(n)
    """
    memo = {}

    def helper(n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n in memo:
            return memo[n]

        memo[n] = helper(n - 1) + helper(n - 2)
        return memo[n]

    return helper(n)


if __name__ == '__main__':
    print(dp(5))
    print(recursion(5))