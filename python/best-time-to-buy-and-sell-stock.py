class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        cur=-1
        r=0
        for i in range(n-1,-1,-1):
            if(cur-prices[i]>r):
                r=cur-prices[i]
            if(prices[i]>cur):
                cur=prices[i]
        return r
            
            
