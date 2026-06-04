class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar, maxprofit = prices[0], 0
        for idx, price in enumerate(prices):
            profit = price - minsofar
            minsofar = min(minsofar, price)
            maxprofit = max(profit, maxprofit)
        return maxprofit