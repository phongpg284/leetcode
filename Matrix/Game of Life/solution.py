class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        new_board = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count = self.neighbor_count(board, i, j)
                print(i, j, count)
                if board[i][j] == 1:
                    if count >= 2 and count <= 3:
                        new_board[i][j] = 1
                else:
                    if count == 3:
                        new_board[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = new_board[i][j]

    def neighbor_count(self, board, i, j):
        directions = [(1, 1), (1, 0), (1, -1), (0, -1),
                      (-1, -1), (-1, 0), (-1, 1), (0, 1)]
        count = 0
        for x, y in directions:
            new_i = i + x
            new_j = j + y
            if new_i >= 0 and new_i < len(board) and new_j >= 0 and new_j < len(board[0]) and board[new_i][new_j] == 1:
                count += 1
        return count
