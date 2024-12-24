class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subchars = set()
        window_size = 0
        maxLen = 0
        for i in range(len(s)):
            window_size += 1
            while s[i] in subchars:
                subchars.remove(s[i-window_size+1])
                window_size -= 1
            subchars.add(s[i])
            maxLen = max(maxLen, window_size)
        return maxLen