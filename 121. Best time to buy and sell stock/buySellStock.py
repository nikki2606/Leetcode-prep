class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, l = 0,0
        
        for r in range(l,len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r]-prices[l])
        return res

### Notes
# Time: O(n)
# Space: O(1)