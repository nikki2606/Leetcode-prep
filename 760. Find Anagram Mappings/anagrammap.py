# Time: O(n) Space: O(n)
class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = []
        nums2Map = {}
        for j,num in enumerate(nums2):
            if num not in nums2Map:
                nums2Map[num] = j
        
        for i,num1 in enumerate(nums1):
            mapping.append(nums2Map[num1])
        
        return mapping