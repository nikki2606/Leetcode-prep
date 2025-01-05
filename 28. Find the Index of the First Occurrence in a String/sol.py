class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if not haystack:
            return -1
        
        m = len(needle)
        n = len(haystack)
        for i in range(n):
            if haystack[i] == needle[0]:
                if haystack[i:i+m] == needle:
                    return i
        return -1