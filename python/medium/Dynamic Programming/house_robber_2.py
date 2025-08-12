def rob(nums: list[int]) -> int:
    """
    LC 213.

    There are 2 scenarios, rubbing the first or the last.
    Compare and return.
    """

    if len(nums) == 1:
        return nums[0]

    first_house_dp = [0 for _ in range(len(nums))]
    last_house_dp = [0 for _ in range(len(nums))]

    first_house_dp[0] = nums[0]
    last_house_dp[0] = nums[1]

    for i in range(1, len(nums)):
        first_house_dp[i] = max(first_house_dp[i - 1], first_house_dp[i - 2] + nums[i - 1])
        last_house_dp[i] = max(last_house_dp[i - 1], last_house_dp[i - 2] + nums[i])


    return max(first_house_dp[-1], last_house_dp[-1])

if '__main__' == __name__:
    print(rob([1,2,1,1]))