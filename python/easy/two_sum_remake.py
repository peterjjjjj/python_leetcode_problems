#The remake of 2sum includes: brute, hash, pointer solutions

def two_sum_brute(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def two_sum_hash(nums: list[int], target: int) -> list[int]:
    #Consists 2 parts, value : i, for i, value in enumerate(nums)
    hash = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash:
            return [hash[diff], i]
        hash[num] = i

def two_sum_pointer(nums: list[int], target: int) -> list[int]:
    #Num i reversed
    nums_index = {num : i for i, num in enumerate(nums)}
    nums.sort()

    i, j = 0, len(nums) - 1

    while i < j:
        if nums[i] + nums[j] == target:
            #Must be no duplicate
            return [nums_index[nums[i]], nums_index[nums[j]]]
        elif nums[i] + nums[j] < target:
            i += 1
        elif nums[i] + nums[j] > target:
            j -= 1

if __name__ == "__main__":
    print(two_sum_brute([2, 7, 11, 15], 9))
    print(two_sum_hash([2, 7, 11, 15], 9))
    print(two_sum_pointer([2, 7, 11, 15], 9))