class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check if row/col contains duplicates
        rowhmap = defaultdict(int)
        colhmap = defaultdict(int)
        boxhmap = defaultdict(int)
        for r in range(0,len(board)):
            for c in range(0, len(board)):
                if(colhmap[board[c][r]] == 1 or rowhmap[board[r][c]] == 1 or boxhmap[(r//3, c//3, board[r][c])] == 1):
                    return False
                if (rowhmap[board[r][c]] == 0 and board[r][c] != "."):
                    rowhmap[board[r][c]] = 1
                if (colhmap[board[c][r]] == 0 and board[c][r] != "."):
                    colhmap[board[c][r]] = 1
                
                if (boxhmap[r//3, c//3, board[r][c]] == 0 and board[r][c] != "."):
                    boxhmap[(r//3, c//3, board[r][c])] = 1
            rowhmap.clear()
            colhmap.clear()

        # Check if sub-box contains duplicates

        return True
