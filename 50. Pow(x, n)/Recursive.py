class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if x == 0:
            return 0.0
        
        if n < 0:
            x = 1/x
            n = abs(n)
            
        if n % 2 == 0:
            return self.myPow(x*x, n//2)
        else:
            return x*self.myPow(x*x, (n-1)//2)

# Time: O(logn)