def rob(nums: list[int]) -> int:
    """
    LC 213.
    """


    #Construct the dp table.
    dp = [0 for _ in range(len(nums))]

    dp[1] = max(nums[0], nums[-1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])


    return dp[-1]

if '__main__' == __name__:
    print(rob([2,3,2]))
    print(rob([1,2,3,1]))
    print(rob([2,1,1,2]))
    print(rob([1,2,3]))