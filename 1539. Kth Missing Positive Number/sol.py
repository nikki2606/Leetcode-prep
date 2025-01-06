class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if not arr:
            return k
        
        if k == 0:
            return 0
        
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid]-(mid+1) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k