class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # diagonal ==> r1-c1 == r2-c2
        if not matrix:
            return True

        diagonals = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in diagonals:
                    diagonals[r-c] = val
                elif diagonals[r-c] != val:
                    return False
        return True

