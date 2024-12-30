from collections import Counter

def ContinuousPath(segments):
    segDict = {}
    flattenSeg = []
    for x,y in segments:
        segDict[x] = y
        flattenSeg.extend([x,y])
    segCount = Counter(flattenSeg)
    endpts = []

    for k,v in segCount.items():
        if v == 1:
            endpts.append(k)
    
    if len(endpts) > 2:
        return []
    
    start = endpts[0]
    if start not in segDict:
        start = endpts[1]
    res = []
    
    for i in range(len(segments)):
        res.append((start, segDict[start]))
        start = segDict[start]
    
    return res

example = [(4, 5), (9, 4), (5, 1), (11, 9)]
print(ContinuousPath(example))