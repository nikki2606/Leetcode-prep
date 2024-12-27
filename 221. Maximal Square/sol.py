class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for j in range(m)] for i in range(n)]
        sqlen = 0
        for i in range(n):
            dp[i][0] = int(matrix[i][0])
            sqlen = max(sqlen, dp[i][0])
        
        for j in range(m):
            dp[0][j] = int(matrix[0][j])
            sqlen = max(sqlen, dp[0][j])
        
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                    sqlen = max(sqlen, dp[i][j])
        
        return sqlen*sqlen

# Time: O(n*m)