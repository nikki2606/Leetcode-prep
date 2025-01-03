class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check Rows
        for i in range(9):
            numSet = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in numSet:
                    return False
                numSet.add(board[i][j])
        
        # check cols
        for j in range(9):
            numSet = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in numSet:
                    return False
                numSet.add(board[i][j])
        
        # check boxes
        '''
                r       c
        i = 0  0 1 2  0 1 2
          = 1  0 1 2  3 4 5
          = 2. 0 1 2  6 7 8
          = 3. 3 4 5  0 1 2
        '''
        for i in range(9):
            numSet = set()
            row1 = i//3 * 3
            row2 = i//3 * 3 + 3
            col1 = i%3 if i%3 == 0 else i%3 * 3
            col2 = i%3 + 3 if i%3 == 0 else i%3 * 3 + 3
            for r in range(row1, row2):
                for c in range(col1, col2):
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in numSet:
                        return False
                    numSet.add(board[r][c])
            
        return True
            