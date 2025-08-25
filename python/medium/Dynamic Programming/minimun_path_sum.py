def min_path_sum(grid: list[list[int]]) -> int:
    """
    LC 64.
    """

    #Initialize the dp table.
    dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    dp[0][0] = grid[0][0]

    #Since you can only move right or down, the first column and first row,
    #Are just summing up to the end.
    for i in range(1, len(grid)):
        dp[i][0] = grid[i][0] + dp[i - 1][0]
    for i in range(1, len(grid[0])):
        dp[0][i] = grid[0][i] + dp[0][i - 1]

    #For the rest of the metrix, the minimum path would be the min of dp from the above, j-1, i, and left, i-1,j.
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[-1][-1]





if __name__ == '__main__':
    #print(min_path_sum([[1,3,1], [1,5,1], [4,2,1]]))
    #print(min_path_sum([[1,2,3], [4,5,6]]))
    print(min_path_sum([[1,2], [1,1]]))