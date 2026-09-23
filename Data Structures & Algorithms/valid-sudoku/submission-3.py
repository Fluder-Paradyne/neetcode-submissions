from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxHash = defaultdict(list)
        colSet = defaultdict(list)
        rowSet = defaultdict(list)
        for i in range(9):
            for j in range(9):
                current = board[i][j]
                if current == ".":
                    continue
                if  current in rowSet[i] or current in colSet[j] or current in boxHash[(i//3, j//3)]:
                    return False
                boxHash[(i//3, j//3)].append(current)
                colSet[j].append(current)
                rowSet[i].append(current)
                
        return True