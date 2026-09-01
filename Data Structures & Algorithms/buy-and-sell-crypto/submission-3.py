class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minBuy = prices[0]

        maxP = 0

        for sell in prices:

            maxP = max(sell - minBuy, maxP)
            minBuy = min(sell, minBuy)
        
        return maxP
            