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

    first_house_dp[1] = nums[0]
    last_house_dp[1] = nums[1]

    #The robbing logic is the same as robbing house 1.
    #The first scenario, rob first not last, is nums[:length - 1].
    #Second scenario, rob last not first, is nums[1:].
    for i in range(2, len(nums)):
        first_house_dp[i] = max(first_house_dp[i - 1], first_house_dp[i - 2] + nums[i - 1])
        last_house_dp[i] = max(last_house_dp[i - 1], last_house_dp[i - 2] + nums[i])


    return max(first_house_dp[-1], last_house_dp[-1])

def rob_2(nums: list[int]) -> int:

    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    def rob_linear(nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0 for _ in range(len(nums) + 1)]
        dp[1] = nums[0]

        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])

        return dp[-1]

    #The robbing logic is the same as robbing house 1.
    #The first scenario, rob first not last, is nums[:length - 1].
    #Second scenario, rob last not first, is nums[1:].
    rob_first = rob_linear(nums[:n - 1])
    rob_last = rob_linear(nums[1:])

    return max(rob_first, rob_last)

if '__main__' == __name__:
    print(rob([2,3,2]))
    print(rob([1,1]))
    print(rob_2([2,3,2]))
    print(rob_2([1,1]))
