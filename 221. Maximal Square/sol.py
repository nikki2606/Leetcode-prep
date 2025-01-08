class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    dp[i][j] += 1
                    if i>0 and j>0:
                        dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        sqlen = 0
        for i in range(n):
            for j in range(m):
                sqlen = max(sqlen, dp[i][j])
        
        return sqlen*sqlen