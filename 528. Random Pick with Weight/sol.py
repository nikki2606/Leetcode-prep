import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.sum_w = 0
        self.prefix = []
        for x in w:
            self.sum_w += x
            self.prefix.append(self.sum_w)

    def pickIndex(self) -> int:
        target = self.sum_w * random.random()
        left, right = 0, len(self.prefix)
        res = 0
        while left < right:
            mid = left + (right-left)//2
            if target > self.prefix[mid]:
                left = mid + 1
            else:
                right = mid
            
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()