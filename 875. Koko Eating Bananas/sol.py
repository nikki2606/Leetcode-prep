class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, 10**9
        speed = 10**9
        while left <= right:
            mid = (left+right)//2
            if self.feasible(piles, h, mid):
                speed = mid
                right = mid - 1
            else:
                left = mid + 1
        return speed
    
    def feasible(self, piles, h, k):
        hours_used = 0
        for pile in piles:
            hours_used += ceil(float(pile)/k)
        return hours_used <= h