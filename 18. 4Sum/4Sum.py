# Time: O(n**3) Space: O(n)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        
        res = []
        lookupSet = set()
        nums = sorted(nums)
        for i in range(n-3):
            for j in range(i+1,n-2):
                left = j+1
                right = n-1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        if (nums[i],nums[j],nums[left],nums[right]) not in lookupSet:
                            lookupSet.add((nums[i],nums[j],nums[left],nums[right]))
                            res.append([nums[i],nums[j],nums[left],nums[right]])
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return res