class Solution:
    def reverse(self, x: int) -> int:
        # Time: O(logx)
        negative = 0
        if x < 0:
            negative = 1
            x = abs(x)
            
        binary = []
        while x:
            binary.append(x%10)
            x //= 10
        res = 0
        for i in range(len(binary)-1, -1, -1):
            place = len(binary)-1-i
            res += (binary[i]*10**place)
        
        if negative:
            res = -res
        if res < -2**31 or res > 2**31-1:
            return 0
        return res