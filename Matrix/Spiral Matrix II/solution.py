class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        pos = [0, 0]
        direction = 0
        i = 0
        while i < n * n:
            i += 1
            matrix[pos[0]][pos[1]] = i
            [next_x, next_y] = self.next(pos, direction)
            if next_x == n or next_y == n or next_x == -1 or next_y == -1 or matrix[next_x][next_y] > 0:
                direction = self.next_direction(direction)
            pos = self.next(pos, direction)
        return matrix           

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