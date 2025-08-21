def length(nums: list[int]) -> int:
    """
    LC 300
    """

    max_subsequence = [nums[0]]

    def binary_search(num: int):
        left = 0
        right = len(max_subsequence) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if max_subsequence[mid] == num:
                return
            elif max_subsequence[mid] < num:
                left = mid + 1
            else:
                right = mid - 1

        max_subsequence[left] = num
        return

    for i in range(1, len(nums)):
        if nums[i] > max_subsequence[-1]:
            max_subsequence.append(nums[i])

        else:
            binary_search(nums[i])

    return len(max_subsequence)

if __name__ == '__main__':
    test_array = [4,10,4,3,8,9]
    print(length(test_array))
