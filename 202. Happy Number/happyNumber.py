class Solution:
    def isHappy(self, n: int) -> bool:
        sumOfSquares = set()
        
        def findSumOfSquares(num):
            ssq = 0
            while num:
                ssq += (num%10)**2
                num = num//10
            return ssq
        
        while n != 1:
            sumOfSquares.add(n)
            n = findSumOfSquares(n)
            if n in sumOfSquares:
                return False
        return True

# Time: O(log n)