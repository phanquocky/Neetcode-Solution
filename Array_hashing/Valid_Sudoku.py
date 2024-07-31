
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
          l = len(board)
          
          # check rows, cols is valid
          for i in range(l):
             col = set()
             row = set()
             for j in range(l):
                # check the rows have any replication and not equal "."
                x = board[i][j]
                if x != "." and x in row:
                    return False
                row.add(x)
              
                # check the cols have any replication and not equal "."
                y = board[j][i]  
                if y != "." and y in col:
                    return False
                col.add(y)

          # check square 9 is valid
          for i in range(l):
              x = i // 3
              y = i % 3
              s = set()
              for j in range(3):
                  for k in range(3):
                      dx = 3 * x + j
                      dy = 3 * y + k
                      v = board[dx][dy]
                      if v != "." and v in s:
                          return False
                      s.add(v)
          return True

board = [["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]

sol = Solution()
print(sol.isValidSudoku(board)) # True