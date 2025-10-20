

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return nums[i], nums[j]


def twoSum2(nums, target):
    sorted_nums = sorted(nums)
    i=0
    j=len(nums)-1
    while i<j:
        sum = sorted_nums[i] + sorted_nums[j]
        if sum == target:
            indices = []
            indices.append(nums.index(sorted_nums[i]))
            for k in range(len(nums)):
                if sorted_nums[j] == nums[k] and k not in indices:
                    indices.append(k)
            return indices
        elif sum > target:
            j=j-1
        elif sum < target:
            i=i+1

    return False


def twoSumHash(nums: list[int], target: int) -> list[int]:
    """
    Review of sum2.
    TC, SC: O(n)
    """

    #{previous num : index}.
    hash_table = {}

    for i, num in enumerate(nums):
        complement = target - num

        # If num could be one of the complements.
        if complement in hash_table:
            return [hash_table[complement], i]

        hash_table[num] = i  # Key: num, Value: index.

    return []


nums = [-1,0,1,2,-1,-4]
#print(twoSum(nums, 0))
#print(twoSum2(nums, 6))
print(twoSumHash([2, 7, 11, 15], 9))