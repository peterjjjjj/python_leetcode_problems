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
        l = 0
        max_profit = 0

        for i in range(1, len(self.prices)):
            if self.prices[l] < self.prices[i]:
                current_profit = self.prices[i] - self.prices[l]
                max_profit = max(max_profit, current_profit)
            else:
                l = i

        return max_profit

if __name__ == "__main__":
    testcase = Solution([7,6,5,4,3,1])
    print(testcase.greedy())
    print(testcase.pointer())