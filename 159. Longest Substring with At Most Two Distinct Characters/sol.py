class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        k = 2
        maxLen = 0
        if len(s) <= k:
            return len(s)

        unique = {}
        start = 0
        for i in range(len(s)):
            if s[i] not in unique:
                unique[s[i]] = 1
            else:
                unique[s[i]] += 1
            
            
            while len(unique) > k:
                if unique[s[start]] > 0:
                    unique[s[start]] -= 1
                if unique[s[start]] == 0:
                    del unique[s[start]]
                start += 1
            maxLen = max(maxLen, i-start+1)
        return maxLen