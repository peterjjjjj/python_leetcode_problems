def find_min(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    if nums[0] > nums[-1]:
        return find_min(nums[len(nums)//2:])

    else:
        return find_min(nums[:len(nums)//2])

if __name__ == '__main__':
    print(find_min([3,4,5,1,2]))
