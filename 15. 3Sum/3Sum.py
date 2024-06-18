# Time: O(n**2) Space:O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        lookupSet = set()
        target = 0
        nums = sorted(nums)
        for i in range(n-2):
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    if (nums[i], nums[left], nums[right]) not in lookupSet:
                        res.append([nums[i], nums[left], nums[right]])
                        lookupSet.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return res