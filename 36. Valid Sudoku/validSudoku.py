class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check1to9Valid(lst):
            digits = set()
            for i in range(9):
                if lst[i] == ".":
                    continue
                elif lst[i] in digits:
                    return False
                else:
                    digits.add(lst[i])
                    
            return True
        
        def getSubBox(m):
            box = []
            i = (m//3)*3
            for j in range(i,i+3):
                a = (m%3)*3
                for k in range(a,a+3):
                    box.append(board[j][k])
            return box
        
        #rows, cols and boxes
        for i in range(9):
            # row
            r = board[:][i]
            
            # col
            c = [row[i] for row in board]
            
            # box
            b = getSubBox(i)
            
            if not (check1to9Valid(r) and check1to9Valid(c)):
                return False
            
            if not (check1to9Valid(b)):
                return False
            
        return True
            

### Notes
# Time: O(n^3)
# Space: O(n)