def max_subarray(nums: list[int]) -> int:
    """
    LC 53
    """

    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        #The dp table represents the max sum of the subarray ends at i.
        dp[i] = nums[i] + max(dp[i - 1], 0)

        max_sum = max(max_sum, dp[i])

    return max_sum

if __name__ == '__main__':
    print(max_subarray([2, -1, -3, 4, -1, 2, 1, -5, 4]))