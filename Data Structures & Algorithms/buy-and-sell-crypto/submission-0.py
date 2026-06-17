class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointer method - start from i=0 and j=1
        # while j<len(prices) -> keep moving j to the right if: 
        # if: prices[j]>prices[i] and keep calculating the profit and max profit so far ..
        # if:  prices[j]<=prices[i] -> move i to j's position and j to i+1 then again do the above steps


        i,j=0,1
        max_profit = 0

        while (j<len(prices)):
            buy = prices[i]
            sell = prices[j]
            if sell>buy:
                profit = sell-buy
                max_profit = max(max_profit, profit)
                j=j+1
            else:
                i=j
                j=i+1
        return max_profit