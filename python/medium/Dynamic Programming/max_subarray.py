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


def max_subarray_dive_n_conquer(nums: list[int]) -> int:
    """
    Divide n conquer solution.
    """


    # Cross sum is the max sum of the subarray cross the midpoint.
    def find_cross_sum(array: list[int]) -> int:
        mid_index = (len(array) - 1) // 2

        #Starts from the midpoint to the sides, find the max sum in left and right.
        current_sum = 0
        left_cross_sum = float('-inf')
        for i in range(mid_index, -1, -1):
            current_sum += array[i]
            left_cross_sum = max(left_cross_sum, current_sum)

        current_sum = 0
        right_cross_sum = float('-inf')
        for i in range(mid_index + 1, len(array), +1):
            current_sum += array[i]
            right_cross_sum = max(right_cross_sum, current_sum)

        cross_sum = left_cross_sum + right_cross_sum

        return cross_sum


    def divide_n_conquer(array: list[int]) -> int:
        if len(array) == 1:
            return array[0]

        mid_index = (len(array) - 1) // 2
        left_max_sum = divide_n_conquer(array[:mid_index + 1])
        right_max_sum = divide_n_conquer(array[mid_index + 1:])
        cross_sum = find_cross_sum(array)

        return max(cross_sum, left_max_sum, right_max_sum)


    return divide_n_conquer(nums)



if __name__ == '__main__':
    print(max_subarray([2, -1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_subarray_dive_n_conquer([2, -1, -3, 4, -1, 2, 1, -5, 4]))