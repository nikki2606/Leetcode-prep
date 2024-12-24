class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countvec_p = [0]*26
        for char in p:
            countvec_p[ord(char)-ord('a')] += 1
        
        countvec_s = [0]*26
        len_p = len(p)
        res = []

        for i in range(len_p):
            if len_p <= len(s):
                countvec_s[ord(s[i])-ord('a')] += 1
        
        if countvec_p == countvec_s:
            res.append(0)

        for i in range(len_p, len(s)):
            countvec_s[ord(s[i-len_p])-ord('a')] -= 1
            countvec_s[ord(s[i])-ord('a')] += 1

            if countvec_p == countvec_s:
                res.append(i-len_p+1)
        
        return res
