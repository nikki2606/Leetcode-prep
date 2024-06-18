# Time: O(n) space: O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        present = set(nums)
        n = len(nums)

        res = []
        for i in range(1,n+1):
            if i not in present:
                res.append(i)
        return res