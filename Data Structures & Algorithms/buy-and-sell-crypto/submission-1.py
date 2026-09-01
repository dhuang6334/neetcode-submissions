class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        localmin = 0
        out = 0
        for i in range(len(prices)):
            if (i > 0):
                if (prices[i] < prices[i-1]):
                    if (prices[i] < prices[localmin]):
                        localmin = i
                else:
                    if (prices[i] - prices[localmin] > out):
                        out = prices[i] - prices[localmin]
        return out

