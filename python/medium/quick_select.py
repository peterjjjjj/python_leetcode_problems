def quick_select(nums, target_position):
    def partition(nums, low, high):
        #i is the index of the partitioned nums that's smaller than pivot
        i = low - 1
        pivot = nums[high]

        #j is the iterator
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]

        #swap pivot to it's correct position
        nums[i + 1], nums[high] = nums[high], nums[i + 1]

        return i + 1

    def select(nums, low, high, target_position):
        if low == high:
            return nums[target_position]

        pivot = partition(nums, low, high)

        if pivot == target_position:
            return nums[pivot]
        elif pivot < target_position:
            low = pivot + 1
            return select(nums, low, high, target_position)
        else:
            high = pivot - 1
            return select(nums, low, high, target_position)

    return select(nums, 0, len(nums) - 1, target_position)

if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    result = quick_select(nums, 3)
    print(result)