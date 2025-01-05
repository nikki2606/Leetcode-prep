class Solution:
    def maxScore(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        prefix_left = [0]*(n-1)
        prefix_right = [0]*(n-1)

        for i in range(n-1):
            if i == 0:
                if s[i] == "0":
                    prefix_left[i] += 1

            elif s[i] == "0":
                prefix_left[i] += (prefix_left[i-1]+1)
            else:
                prefix_left[i] = prefix_left[i-1]
        
        for i in range(n-1,0,-1):
            if i == n-1:
                if s[i] == "1":
                    prefix_right[i-1] += 1
            elif s[i] == "1":
                prefix_right[i-1] += (prefix_right[i]+1)
            else:
                prefix_right[i-1] = prefix_right[i]
        
        ways = 0
        for i in range(n-1):
            ways = max(ways, prefix_left[i]+prefix_right[i])
        return ways