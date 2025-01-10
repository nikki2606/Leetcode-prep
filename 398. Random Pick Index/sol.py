from collections import defaultdict
class Solution:

    def __init__(self, nums: List[int]):
        self.numIdx = defaultdict(list)
        for i,num in enumerate(nums):
            self.numIdx[num].append(i)


    def pick(self, target: int) -> int:
        idx = random.choice(self.numIdx[target])
        return idx


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)