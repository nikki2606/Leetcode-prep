class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 4:
            return arr[0]
        
        target1, target2, target3 = arr[n//4], arr[n//2], arr[3*n//4]

        for target in [target1, target2, target3]:
            if self.binsearch(target, arr) > n//4:
                return target
        
        return target1

    def binsearch(self, target, arr):
        # first pos
        left, right = 0, len(arr)-1
        first = 0
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == target:
                first = mid
                right = mid - 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            
        # last pos
        left, right = 0, len(arr)-1
        last = len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == target:
                last = mid
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return last-first+1