class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)] 
        sub = [set() for _ in range(9)] 

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in sub[3*(i//3) + (j//3)]:
                    print(board[i][j] + " " + str(i) + "," + str(j))
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    sub[3* (i//3) + (j//3)].add(board[i][j])

        return True