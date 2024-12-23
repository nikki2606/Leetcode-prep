class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        if n < 2:
            return n

        k = 1
        curr = 0
        for i in range(1,n):
            if nums[curr] == nums[i]:
                continue

            k += 1
            curr += 1
            nums[curr] = nums[i]
        return k