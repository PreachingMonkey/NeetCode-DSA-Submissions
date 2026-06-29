class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isValid = True
        visited = set()
# Col
        for i in range(0,9):
            visited.clear()
            for j in range(0,9):
                if board[i][j]==".":
                    continue
                elif (board[i][j]) in visited:
                    isValid=False
                    return isValid
                else:
                    visited.add(board[i][j])
            
# Row 
        for i in range(0,9):
            visited.clear()
            for j in range(0,9):
                if board[j][i]==".":
                    continue
                elif (board[j][i]) in visited:
                    isValid=False
                    return isValid
                else:
                    visited.add(board[j][i])

        
        for i in range(0,9):
            visited.clear()
            for j in range(3):
                for k in range(3):
                    row = (i//3)*3 + j
                    col = (i % 3)*3 + k
                    if board[row][col]==".":
                        continue
                    elif board[row][col] in visited:
                        isValid=False
                        return isValid
                    else:
                        visited.add(board[row][col])
                        
        return isValid


                