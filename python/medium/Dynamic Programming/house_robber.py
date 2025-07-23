def rob(nums: list[int]) -> int:
    """
    See LC problem 198.

    :param nums: list[int]
    :return: int
    """

    #Initialize the dp table.
    dp = [0 for _ in range(len(nums) + 1)]
    dp[1] = nums[0]

    for i in range(1, len(nums)):
        #The index in the dp table.
        dp_index = i + 1
        #Cuz you cannot rob 2 adjacent houses, either you rob the previous house(dp[dp_index - 1] or this house.
        #Rubbing this house means you get to rub house before the previous house which is nums[i] + dp[dp_index - 2].
        dp[dp_index] = max(nums[i] + dp[dp_index - 2], dp[dp_index - 1])

    return dp[-1]

if __name__ == '__main__':
    assert rob([1, 2, 3, 1]) == 4