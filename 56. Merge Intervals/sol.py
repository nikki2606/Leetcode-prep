class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])

        res = []
        for start, end in intervals:
            if not res:
                res.append([start,end])
            else:
                if res[-1][-1] < start:
                    res.append([start,end])
                elif res[-1][-1] < end:
                    start_temp, end_temp = res.pop()
                    res.append([start_temp, end])
                else:
                    continue
        return res