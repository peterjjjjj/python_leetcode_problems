def rob(nums: list[int]) -> int:
    """
    LC 213.
    """

    #Construct the dp table.
    dp = [0 for _ in range(len(nums) + 1)]

    if len(nums) % 2 == 0:
        dp[1] = nums[0]

    for i in range(2, len(nums) + 1):
        dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])

    return dp[-1]

if '__main__' == __name__:
    print(rob([2,3,2]))
    print(rob([1,2,3,1]))