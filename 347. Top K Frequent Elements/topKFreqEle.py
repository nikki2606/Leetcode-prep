class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums
        
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        
        sortedD = {k:v for k,v in sorted(d.items(), key= lambda item:item[1], reverse=True)}
        lstD = [v for v in sortedD.keys()]
        return lstD[:k]

### Notes
# Time: O(n)
# Space:O(1)