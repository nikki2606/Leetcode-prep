from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        INF = 2147483647
        queue = deque()
        n = len(rooms)
        m = len(rooms[0])
        for i, map_row in enumerate(rooms):
            for j, entry in enumerate(map_row):
                if entry == 0:
                    queue.append((i, j))
        while queue:
            row, col = queue.popleft()
            for delta_row, delta_col in directions:
                total_row, total_col = row + delta_row, col + delta_col
                if total_row >= 0 and total_row < n and total_col >= 0 and total_col < m:
                    if rooms[total_row][total_col] == INF:
                        rooms[total_row][total_col] = rooms[row][col] + 1
                        queue.append((total_row, total_col))
# Time: O(n*m)