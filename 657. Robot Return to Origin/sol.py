class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if not moves:
            return False

        x, y = 0, 0
        for move in moves:
            if move == "R":
                x += 1
            elif move == "L":
                x -= 1
            elif move == "U":
                y += 1
            elif move == "D":
                y -= 1
            else:
                return False
        
        return x == 0 and y == 0