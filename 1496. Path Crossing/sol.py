# Time: O(n) Space: O(n)
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pathxy = set()
        point = [0,0]
        pathxy.add(tuple(point))

        for d in path:
            if d == 'N':
                point[1] += 1
            elif d == 'S':
                point[1] -= 1
            elif d == 'E':
                point[0] += 1
            else:
                point[0] -= 1
            
            if tuple(point) in pathxy:
                return True

            pathxy.add(tuple(point))
        
        return False