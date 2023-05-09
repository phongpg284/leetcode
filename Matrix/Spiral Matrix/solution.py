class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        path = []
        m = len(matrix)
        n = len(matrix[0])
        pos = [0, 0]
        direction = 0
        while len(path) < m * n:
            path.append(matrix[pos[0]][pos[1]])
            matrix[pos[0]][pos[1]] = -101
            [next_x, next_y] = self.next(pos, direction)
            if next_x == m or next_y == n or next_x == -1 or next_y == -1 or matrix[next_x][next_y] == -101:
                direction = self.next_direction(direction)
            pos = self.next(pos, direction)
        return path           

    def next(self, pos, direction):
        if direction == 0:
            return [pos[0], pos[1] + 1]
        if direction == 1:
            return [pos[0] + 1, pos[1]]
        if direction == 2:
            return [pos[0], pos[1] - 1]
        return [pos[0] - 1, pos[1]]

    def next_direction(self, direction):
        if direction == 3:
            return 0
        return direction + 1