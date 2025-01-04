class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        1 3 4 2
              i
        stack = 
        d = {1:3, 3:4, 2:-1, 4:-1}
        '''
        stack = []
        greaterDict = {}
        for i in range(len(nums2)):
            while stack:
                if stack[-1] < nums2[i]:
                    val = stack.pop()
                    greaterDict[val] = nums2[i]
                else:
                    break
            stack.append(nums2[i])
        
        while stack:
            val = stack.pop()
            greaterDict[val] = -1
        
        res = []
        for num in nums1:
            res.append(greaterDict[num])
        return res