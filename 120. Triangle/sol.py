class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0 for j in range(i+1)] for i in range(len(triangle))]
        for i in range(len(triangle)):
            if i == 0:
                dp[i][0] = triangle[i][0]
                continue
            dp[i][0] = dp[i-1][0] + triangle[i][0]

        for i in range(1, len(triangle)):
            for j in range(1, i+1):
                if i-1 < j:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                    continue
                dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j-1])
        
        return min(dp[-1])
# Time: O(n*m)