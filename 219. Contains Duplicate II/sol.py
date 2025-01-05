class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numSet = set()
        for i, num in enumerate(nums):
            if num in numSet:
                return True
            numSet.add(num)
            if len(numSet) > k:
                numSet.remove(nums[i-k])
        return False