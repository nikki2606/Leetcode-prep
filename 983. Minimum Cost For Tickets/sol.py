class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0]*(days[-1]+1)
        travelDays = set(days)
        for day in range(1,len(dp)):
            if day not in travelDays:
                dp[day] = dp[day-1]
            else:
                dp[day] = min(dp[day-1]+costs[0], dp[max(0,day-7)]+costs[1], dp[max(0,day-30)]+costs[2])
        return dp[-1]