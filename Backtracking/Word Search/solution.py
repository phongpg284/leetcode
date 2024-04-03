class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        for i in range(m):
            for j in range(n):
                if self.helper(board, i, j, 0, word, visited, direction):
                    return True

        return False

    def helper(self, board, i, j, k, word, visited, direction):
        if k == len(word):
            return True

        if board[i][j] != word[k]:
            return False

        visited[i][j] = True

        for x, y in direction:
            new_x = i + x
            new_y = j + y
            if (
                0 <= new_x < len(board)
                and 0 <= new_y < len(board[0])
                and not visited[new_x][new_y]
            ):
                if self.helper(board, new_x, new_y, k + 1, word, visited, direction):
                    return True

        visited[i][j] = False

        return k == len(word) - 1
