class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        minim = prices[0]
        while i < len(prices):
            if prices[i] < minim:
                minim = prices[i]
            profit = max(profit, prices[i] - minim)
            i += 1
        return profit