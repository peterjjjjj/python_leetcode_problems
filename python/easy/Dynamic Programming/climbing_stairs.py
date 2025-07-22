def climb_stairs(n: int) -> int:
    """
    You are climbing a staircase, takes n steps to reach the top.
    Each time you climb 1 or 2 steps, how many ways can u climb to the top.

    :param n: int
    return: int
    """

    if n == 1:
        return 1

    dp = []
    dp.append(1)
    dp.append(2)

    for i in range(3, n+1):
        dp.append(
            dp[i-2] + dp[i-3]
        )

    return dp[-1]

if __name__ == '__main__':
    print(climb_stairs(2))
