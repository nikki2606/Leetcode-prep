class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix:
            return True
        
        n = len(matrix)
        m = len(matrix[0])
        if m == 1 or n == 1:
            return True

        # check along row 0
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i-1][j-1] != matrix[i][j]:
                    return False
        return True