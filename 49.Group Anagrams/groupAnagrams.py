class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            sortedW = tuple(sorted(word))
            if sortedW not in d:
                d[sortedW] = []
            d[sortedW].append(word)
        
        res = []
        for lst in d.values():
            res.append(lst)
        return res

### Notes
# Time: O(n)
# Space: O(n)