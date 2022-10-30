class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        negative = 0
        if n < 0:
            negative = 1
            
        n = abs(n)
        res = 1
        while n:
            res *= x
            n -= 1
        
        if negative:
            res = 1/res
        return res

# Time: O(n)