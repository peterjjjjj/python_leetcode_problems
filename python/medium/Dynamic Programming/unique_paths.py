def unique_paths(m: int, n: int) -> int:
    """
    LC 62.
    """

    #Construct the table.
    dp = [[0 for _ in range(n)] for _ in range(m)]

    #The first row always has 1 path, which is all the way to the right.
    for i in range(n):
        dp[0][i] = 1

    #Same with first column.
    for i in range(m):
        dp[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]

if __name__ == '__main__':
    print(unique_paths(3, 7))