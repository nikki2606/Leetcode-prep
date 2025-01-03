class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = [i for i in range(len(s)) if s[i] == "|"]
        res = []

        for qleft, qright in queries:
            if qleft == qright:
                res.append(0)
                continue
            lcandle, rcandle = self.nearest_right(qleft, candles), self.nearest_left(qright, candles)
            candles_in_btw = rcandle - lcandle - 1 if rcandle > lcandle else 0
            plates = candles[rcandle] - candles[lcandle] - 1 - candles_in_btw if rcandle > lcandle else 0
            res.append(plates)
        
        return res
    
    def nearest_right(self, x, candles):
        left, right = 0, len(candles)-1
        out = 0
        while left <= right:
            mid = (left+right)//2
            if candles[mid] >= x:
                out = mid
                right = mid - 1
            else:
                left = mid + 1
        return out

    def nearest_left(self, x, candles):
        left, right = 0, len(candles)-1
        out = len(candles)-1
        while left <= right:
            mid = (left+right)//2
            if candles[mid] <= x:
                out = mid
                left = mid + 1
            else:
                right = mid - 1
        return out