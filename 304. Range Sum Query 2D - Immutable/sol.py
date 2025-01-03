class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        
        if not len(matrix) or not len(matrix[0]):
            return

        row = len(matrix)
        col = len(matrix[0])    
        self.range = [[0 for c in range(col+1)] for r in range(row+1)]
        for r in range(row):
            prefix = 0
            for c in range(col):
                prefix += matrix[r][c]
                self.range[r+1][c+1] = prefix + self.range[r][c+1]
        print(self.range)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.range[row2+1][col2+1] - self.range[row1][col2+1] - self.range[row2+1][col1] + self.range[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)