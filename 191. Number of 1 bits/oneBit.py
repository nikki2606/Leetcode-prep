class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time: O(1)
        count = 0
        mask = 1
        for i in range(32):
            if n & mask != 0:
                count += 1
            mask <<= 1
        return count
        