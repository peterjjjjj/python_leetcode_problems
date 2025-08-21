def length(nums: list[int]) -> int:
    """
    LC 300
    """

    max_subsequence = [nums[0]]

    def binary_search(num: int) -> None:
        left = 0
        right = len(max_subsequence)

        while left <= right:
            mid = left + (right - left) // 2
            if num == max_subsequence[mid]:
                return
            elif num < max_subsequence[mid]:
                if num > max_subsequence[mid - 1]:
                    max_subsequence[mid] = num
                    return
                else:
                    right = mid - 1
            else:
                left = mid + 1

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
