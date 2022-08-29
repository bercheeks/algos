class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxRes = 0
        if len(prices) == 1:
            return maxRes
        
        for i in range(len(prices) -1):
            if prices[i] < prices[i + 1]:
                maxRes = max(maxRes, prices[i+1] - prices[i])
                prices[i+1] = prices[i]
        return maxRes