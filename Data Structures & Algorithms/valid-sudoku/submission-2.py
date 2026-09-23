from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxHash = defaultdict(list)
        colSet = defaultdict(list)
        for i in range(9):
            for j in range(9):
                current = board[i][j]
                if current == ".":
                    continue
                if current in boxHash[(i//3, j//3)] or board[i].count(current) > 1 or current in colSet[j]:
                    return False
                boxHash[(i//3, j//3)].append(current)
                colSet[j].append(current)
                
        return True
