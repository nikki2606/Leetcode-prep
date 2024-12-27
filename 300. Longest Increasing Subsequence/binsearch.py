class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        if not nums:
            return 0

        for num in nums:
            i = self.binsearch(sub, num)

            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        
        return len(sub)
    
    def binsearch(self, arr, target):
        if not arr:
            return 0
        
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left