class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)-1):
            profit = max(prices[i+1:]) - prices[i]
            maxProfit = max(maxProfit, profit)
        return maxProfit

