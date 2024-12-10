class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return [[]]
        m = len(matrix)
        n = len(matrix[0])
        res = [[0 for r in range(m)] for c in range(n)]
        for r in range(m):
            for c in range(n):
                res[c][r] = matrix[r][c]
        return res