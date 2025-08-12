def unique_paths(obstacleGrid: list[list[int]]) -> int:
    """
    Leetcode 63.
    """

    #Initialize the dp table.
    dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

    #Initialize the first row and column.
    #If obstacle encountered, break that loop.
    for i in range(len(obstacleGrid)):
        if obstacleGrid[i][0] == 1:
            break

        dp[i][0] = 1

    for i in range(len(obstacleGrid[0])):
        if obstacleGrid[0][i] == 1:
            break

        dp[0][i] = 1

    #Same logic as Unique Path 1.
    for i in range(1, len(obstacleGrid)):
        for j in range(1, len(obstacleGrid[0])):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0

            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]

