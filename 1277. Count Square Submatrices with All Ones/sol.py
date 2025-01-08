class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    dp[i][j] += 1
                    if i > 0 and j > 0:
                        dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        summ = 0
        for i in range(n):
            for j in range(m):
                summ += dp[i][j]

        return summ