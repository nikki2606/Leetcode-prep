class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''

        -1 0 1
        0 1 2
        '''
        # Count sort
        maxVal = max(nums)
        minVal = min(nums)
        arr = [0]*(maxVal-minVal+1)

        for num in nums:
            arr[num-minVal] += 1
        
        for i in range(len(arr)-1,-1,-1):
            k -= arr[i]
            if k <= 0:
                return i+minVal
        return -1