from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        if grid[0][0] or grid[-1][-1]:
            return -1
        
        a = len(grid)
        b = len(grid[0])
        if a == 1 and b == 1:
            return 1
        queue = deque([[0,0]])
        res = 0
        dir = [[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1], [0,-1], [1,-1]]
        while queue:
            n = len(queue)
            res += 1
            for i in range(n):
                x, y = queue.popleft()
                for j in range(8):
                    x_new = x+dir[j][0]
                    y_new = y+dir[j][1]

                    if x_new < 0 or x_new >= a or y_new < 0 or y_new >= b:
                        continue
                    
                    if grid[x_new][y_new] == 1:
                        continue

                    if x_new == a-1 and y_new == b-1:
                        return res+1
                    
                    grid[x_new][y_new] = 1

                    queue.append([x_new,y_new])
        return -1