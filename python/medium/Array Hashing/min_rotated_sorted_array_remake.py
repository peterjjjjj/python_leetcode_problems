def binary_search(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        #The min of array is after highest, if mid > right, array ends and then starts in right half
        if nums[mid] > nums[right]:
            left = mid + 1

        #This section is continuous, min is in [left, mid]
        elif nums[mid] < nums[right]:
            right = mid

    #After while left == right
    return nums[left]


def binary_search_recursion(nums: list[int]) -> int:

    def helper(low: int, high: int) -> int:
        if low == high:
            return nums[low]

        mid = (low + high) // 2

        if nums[mid] > nums[high]:
            return helper(mid + 1, high)

        elif nums[mid] < nums[high]:
            return helper(low, mid)

    return helper(0, len(nums) - 1)

def practice_recursion(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    def helper(low: int, high: int) -> int:
        if low == high:
            return nums[low]

        mid = (low + high) // 2

        if nums[mid] > nums[high]:
            return helper(mid + 1, high)

        elif nums[mid] < nums[high]:
            return helper(low, mid)

    return helper(left, right)


if __name__ == '__main__':
    print(binary_search([3,4,0,1,2]))
    print(binary_search_recursion([3,4,0,1,2]))
    print(practice_recursion([3,4,5,0,1,2]))