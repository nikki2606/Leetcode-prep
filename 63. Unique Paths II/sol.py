class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        
        for j in range(m):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] += dp[i-1][j] + dp[i][j-1]
        
        return dp[n-1][m-1]