class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = float('-inf')
        sell = 0
        '''
            Buy and sell represent maximum profit for current day if own a stock or not
        '''
        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)
        return sell