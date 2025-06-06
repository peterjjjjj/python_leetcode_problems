def find_min(nums: list[int]) -> int:
    low_bound = 0
    high_bound = len(nums) - 1

    def search(nums:list[int]) -> int:
        nonlocal low_bound, high_bound

        if low_bound == high_bound:
            return nums[low_bound]

        #mid num of the array
        mid_index = (low_bound + high_bound) // 2

            #if mid num smaller than left bound, smaller array on the right
        if nums[mid_index] > nums[high_bound]:
            low_bound = mid_index + 1
            return search(nums)
        else:
            high_bound = mid_index
            return search(nums)

    return search(nums)
if __name__ == '__main__':
    print(find_min([4,5,6,7,0,1,2]))
