def length(nums: list[int]) -> int:
    """
    LC 300
    """

    #Initialize the dp table.
    dp = [0 for _ in range(len(nums) + 1)]
    #The length should be at least 1.
    dp[1] = 1

    max_len = 1
    previous_max = dp[1]

    if len(nums) == 1:
        return dp[1]


    for i in range(2, len(nums) + 1):
        if nums[i - 1] > nums[i - 2] and nums[i - 1] > previous_max:
            dp[i] = dp[i - 1] + 1
            previous_max = nums[i - 1]
            if dp[i] > max_len:
                max_len = dp[i]

        else:
            dp[i] = 1
            previous_max = nums[i - 1]

    return max_len

if __name__ == '__main__':
    test_array = [4,10,4,3,8,9]
    print(length(test_array))