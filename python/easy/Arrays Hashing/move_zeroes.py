#2 passes, 1 pass

class Solution:
    def __init__(self, nums: list[int]) -> None:
        self.nums = nums

    def two_passes(self) -> list[int]:
        i = 0
        position = 0

        while i < len(self.nums):
            if self.nums[i] != 0:
                self.nums[position] = self.nums[i]
                position += 1
            i += 1

        for i in range(position, len(self.nums)):
            self.nums[i] = 0

        return self.nums

    def one_pass(self) -> list[int]:
        slow_pointer = 0

        for fast_pointer in range(len(self.nums)):
            if self.nums[fast_pointer] != 0:
                self.nums[slow_pointer], self.nums[fast_pointer] = self.nums[fast_pointer], self.nums[slow_pointer]
                slow_pointer += 1

        return self.nums


if __name__ == "__main__":
    testcase = Solution([0,1,0,3,12])
    print(testcase.two_passes())
    testcase2 = Solution([0,1,0,3,12])
    print(testcase2.one_pass())