class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandiesBeforeExtra = max(candies)
        res = []
        for kid in candies:
            kid += extraCandies
            if kid >= maxCandiesBeforeExtra:
                res.append(True)
            else:
                res.append(False)
        return res