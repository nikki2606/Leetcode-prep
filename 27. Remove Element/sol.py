class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_freq = 0
        n = len(nums)
        i = 0
        right = n-1
        while i < (n-val_freq):
            if nums[i] == val:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                val_freq += 1
            else:
                i += 1
        return n-val_freq