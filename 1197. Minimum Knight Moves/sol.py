from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        level = 0 
        queue = deque([[0,0]])
        visited = set(tuple([0,0]))
        while len(queue) > 0:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                for nx, ny in self.get_moves(node[0],node[1]):
                    if nx == x and ny == y:
                        return level+1
                    if tuple([nx,ny]) in visited:
                        continue
                    visited.add(tuple([nx,ny]))
                    queue.append([nx,ny])
            level += 1
        return level

    def get_moves(self, a, b):
        res = []
        for r,c in [[2,1], [1,2], [-1,2], [-2,1], [-1,-2], [-2,-1], [1,-2], [2,-1]]:
            res.append([a+r, b+c])
        return res