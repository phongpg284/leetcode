class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        sub = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j]) - 1
                    sub_index = j // 3 + (i // 3) * 3
                    if row[i][val] or col[j][val] or sub[sub_index][val]:
                        return False
                    row[i][val] = True
                    col[j][val] = True
                    sub[sub_index][val] = True
        return True