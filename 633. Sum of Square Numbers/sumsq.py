# Time: O(n) Space: O(1)
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while c - a*a >= 0:
            b = c - a*a
            sqrt_b = int(math.sqrt(b))
            if b == sqrt_b*sqrt_b:
                return True
            a += 1
        return False