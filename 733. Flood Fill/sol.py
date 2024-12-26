from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        image[sr][sc] = color
        queue = deque([[sr,sc]])
        visited = set(tuple([sr,sc]))
        while len(queue) > 0:
            n = len(queue)
            for i in range(n):
                x, y = queue.popleft()
                for neighbor in self.get_neighbors(x,y,image):
                    if tuple(neighbor) in visited:
                        continue
                    
                    if image[neighbor[0]][neighbor[1]] == old_color:
                        image[neighbor[0]][neighbor[1]] = color
                    else:
                        continue
                    visited.add(tuple(neighbor))
                    queue.append(neighbor)
        return image
    
    def get_neighbors(self, x, y, image):
        n = len(image)
        m = len(image[0])
        res = []
        for r, c in [[1,0], [0,1], [-1,0], [0,-1]]:
            if 0 <= x+r < n and 0 <= y+c < m:
                res.append([x+r, y+c])
        return res
    
# Time : O(N)