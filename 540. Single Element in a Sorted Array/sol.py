class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def to_the_left(idx):
            if idx == len(nums)-1:
                return True
            if (idx % 2):
                return nums[idx] != nums[idx-1]
            else:
                return nums[idx] != nums[idx+1]
                
        left, right = 0, len(nums)-1
        idx = -1
        while left <= right:
            mid = (left+right)//2
            if to_the_left(mid):
                idx = mid
                right = mid - 1
            else:
                left = mid + 1
        return nums[idx]