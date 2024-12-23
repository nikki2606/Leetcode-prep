class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        n = len(nums)
        if n < 2:
            return

        curr = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[curr] = nums[curr], nums[i]
                curr += 1