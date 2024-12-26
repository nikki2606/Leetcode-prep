class Solution:
    def isUgly(self, n: int) -> bool:
        return self.uglyNum(n)

    def uglyNum(self, n):
        if n == 0:
            return False
            
        while n:
            if n%2 == 0:
                n = n//2
            elif n%3 == 0:
                n = n//3
            elif n%5 == 0:
                n = n//5
            elif n == 1:
                return True
            else:
                return False
        return True
# Time: O(logN)