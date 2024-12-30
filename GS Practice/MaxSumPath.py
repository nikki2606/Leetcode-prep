def maxPath(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[0 for j in range(m+1)] for i in range(n+1)]

    # bottom-left to top-right
    # for i in range(n-1,-1,-1):
    #     for j in range(1,m+1):
    #         dp[i][j] = grid[i][j-1] + max(dp[i][j-1], dp[i+1][j])
    # return dp[0][-1]

    # top-left to bottom-right
    # for i in range(1,n+1):
    #     for j in range(1,m+1):
    #         dp[i][j] = grid[i-1][j-1] + max(dp[i-1][j], dp[i][j-1])
    # return dp[-1][-1]

    # bottom-right to top-left
    # for i in range(n-1,-1,-1):
    #     for j in range(m-1,-1,-1):
    #         dp[i][j] = grid[i][j] + max(dp[i+1][j], dp[i][j+1])
    # return dp[0][0]