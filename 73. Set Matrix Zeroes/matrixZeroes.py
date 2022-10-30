class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Time :(n^2)
        copyMatrix = []
        for i in range(len(matrix)):
            copyMatrix.append([])
            for j in range(len(matrix[0])):
                copyMatrix[i].append(matrix[i][j])
                
        def setRowColumnZero(r, c):
            for i in range(len(matrix[0])):
                matrix[r][i] = 0
            
            for j in range(len(matrix)):
                matrix[j][c] = 0
        
        for r in range(len(copyMatrix)):
            for c in range(len(copyMatrix[0])):
                if copyMatrix[r][c] == 0:
                    setRowColumnZero(r,c)