# Time: O(n) Space: O(n)
from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numCount = defaultdict(int)
        for num in arr:
            if num not in numCount:
                numCount[num] = 0
            numCount[num] += 1
        
        freq = list(numCount.values())
        unique = set()
        for f in freq:
            if f in unique:
                return False
            unique.add(f)
        return True