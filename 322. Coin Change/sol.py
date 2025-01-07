class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for amt in range(amount+1):
            for c in coins:
                if amt-c >= 0:
                    dp[amt] = min(dp[amt], 1+dp[amt-c])
        return dp[amount] if dp[amount] != float('inf') else -1