import math
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(int(sqrt(n))+1)]
        dp = [10000 for i in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            for sq in squares:
                if i < sq:
                    break
                dp[i] = min(dp[i], dp[i-sq]+1)
        return dp[n]