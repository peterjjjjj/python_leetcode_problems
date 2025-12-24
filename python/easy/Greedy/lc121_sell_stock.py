#greedy, pointer

class Solution:
    def __init__(self, prices: list[int]) -> None:
        self.prices = prices

    def greedy(self) -> int:
        max_profit = 0
        min_price = self.prices[0]

        for price in self.prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

    def pointer(self) -> int:
        min_index = 0
        max_index = 1

        for i in range(1, len(self.prices)):
            if self.prices[i] < self.prices[min_index]:
                min_index = i
            elif self.prices[i] > self.prices[max_index]:
                max_index = i

        return self.prices[max_index] - self.prices[min_index]


if __name__ == "__main__":
    testcase = Solution([10, 1, 5, 2])
    print(testcase.greedy())
    print(testcase.pointer())