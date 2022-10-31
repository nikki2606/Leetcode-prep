class Solution:
    def countBits(self, n: int) -> List[int]:
        # Time: O(n)
        res = []
        
        def countOnes(m):
            count = 0
            mask = 1
            for i in range(32):
                if m & mask != 0:
                    count += 1
                mask <<= 1
            return count
        
        for i in range(n+1):
            res.append(countOnes(i))
        
        return res