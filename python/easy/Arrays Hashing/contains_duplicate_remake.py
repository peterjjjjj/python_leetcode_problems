#3 solutions: sorted, hash, set

class ContainsDuplicateSolutionsRemake:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def sorted(self) -> bool:
        self.nums.sort()

        for i in range(len(self.nums) - 1):
            if self.nums[i] == self.nums[i+1]:
                return True

        return False

    def hash(self) -> bool:
        hash_table = {}

        for num in self.nums:
            #Check num in keys
            if num in hash_table:
                return True
            hash_table[num] = -1

        return False

    def set(self) -> bool:
        return len(set(self.nums)) < len(self.nums)

if __name__ == '__main__':
    test_case = ContainsDuplicateSolutionsRemake(nums=[1,2,3,1])
    print(test_case.sorted())
    print(test_case.hash())
    print(test_case.set())