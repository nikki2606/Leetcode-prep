# Time: O(n) Space: O(n)
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = set()
        for city in paths:
            source.add(city[0])

        for src, dest in paths:
            if dest not in source:
                return dest
        
        return ""