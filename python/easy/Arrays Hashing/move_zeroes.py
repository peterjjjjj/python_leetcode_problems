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
        zero_positions = []

        for i in range(len(self.nums)):
            if self.nums[i] == 0:
                zero_positions.append(i)
            elif zero_positions:
                self.nums[zero_positions.pop()] = self.nums[i]
                zero_positions.append(i)

        return self.nums


if __name__ == "__main__":
    testcase = Solution([0,1,0,3,12])
    print(testcase.two_passes())
    print(testcase.one_pass())