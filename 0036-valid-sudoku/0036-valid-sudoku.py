class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        sq=defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in cols[i] or board[i][j] in rows[j] or board[i][j] in sq[(i//3,j//3)]:
                    return False
                else:
                    cols[i].add(board[i][j])
                    rows[j].add(board[i][j])
                    sq[(i//3,j//3)].add(board[i][j])
        return True