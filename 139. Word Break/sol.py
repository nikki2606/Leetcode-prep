class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}

        def dfs(start):
            if start == n:
                return True

            if start in memo:
                return memo[start]
            
            res = False
            for word in wordDict:
                if s[start:].startswith(word):
                    if dfs(start+len(word)):
                        res = True
                        break

            memo[start] = res
            return res

        res = dfs(0)
        return res