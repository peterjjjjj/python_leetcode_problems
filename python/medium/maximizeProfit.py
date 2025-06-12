"""
tc: O(n^2) O(n) O(n)
sc: O(1) O(1) O(1)
"""

def maxProfitBrute(prices):
    maxProfit = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j] - prices[i] > maxProfit:
                maxProfit = prices[j] - prices[i]

    return maxProfit

def maxProfit(prices):
    maxProfit = -1
    minPrice = prices[0]
    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        if prices[i] - minPrice > maxProfit:
            maxProfit = prices[i] - minPrice

    return maxProfit

def maxProfitKadane(prices):
    min_price = prices[0]
    max_profit = 0
    diff = 0
    for i in range(1, len(prices)):
        diff += prices[i] - prices[i-1]
        if diff > max_profit:
            max_profit = diff

        if prices[i] < min_price:
            min_price = prices[i]
            diff = 0

    return max_profit

if __name__ == '__main__':
    print(maxProfitBrute([7, 1, 5, 3, 6, 4]))
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfitKadane([7, 1, 5, 3, 6, 4]))