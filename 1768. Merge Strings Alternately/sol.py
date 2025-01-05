class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        
        if not word2:
            return word1
        
        n = len(word1)
        m = len(word2)
        res = ""
        for i in range(min(n,m)):
            res += word1[i] + word2[i]

        if n > m:
            res += word1[m:]
        elif n < m:
            res += word2[n:]
        
        return res