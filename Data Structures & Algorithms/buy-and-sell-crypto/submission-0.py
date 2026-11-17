class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        buy = prices[0]
        for i in prices:
            #print("each_price",i)
            #print("prices[i]",prices[i])
            buy = min(buy,i)
            #print("minprice",buy)
          
            maxprofit = max(maxprofit,i-buy)
        return maxprofit
        