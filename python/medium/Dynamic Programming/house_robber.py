def rob(nums: list[int]) -> int:
    """
    See LC problem 198.

    :param nums: list[int]
    :return: int
    """

    dp = [0 for _ in range(len(nums) + 1)]
    dp[1] = nums[0]

    for i in range(1, len(nums)):
        dp_index = i + 1
        dp[dp_index] = max(nums[i] + dp[dp_index - 2], dp[dp_index - 1])

    return dp[-1]

if __name__ == '__main__':
    assert rob([1, 2, 3, 1]) == 4