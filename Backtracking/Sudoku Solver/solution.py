class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.helper(board, 0, 0)

    def helper(self, board, x, y):
        if x == 9:
            return True

        if board[x][y] != '.':
            next_x, next_y = self.next_step(x, y)
            return self.helper(board, next_x, next_y)

        for i in range(1, 10):
            if self.valid(board, x, y, str(i)):
                board[x][y] = str(i)
                next_x, next_y = self.next_step(x, y)
                if self.helper(board, next_x, next_y):
                    return True
        board[x][y] = '.'
        return False

    def valid(self, board, x, y, val):
        for i in range(9):
            if val == board[x][i] or val == board[i][y] or val == board[x // 3 * 3 + i // 3][y // 3 * 3 + i % 3]:
                return False
        return True

    def next_step(self, x, y):
        if y < 8:
            return x, y + 1
        else:
            return x + 1, 0
