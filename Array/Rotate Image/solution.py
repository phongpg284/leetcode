class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range((len(matrix) + 1) // 2):
            self.rotate_layer(matrix, i)

    def rotate_layer(self, matrix, n):
        matrix_len = len(matrix)
        steps = matrix_len * 4 - 4

        direction = 0
        coord = (n, n)
        q = list()
        limit_coord = (n, matrix_len - 1 - n, n, matrix_len - 1 - n)

        for i in range(steps):
            coord, direction = self.next_coord(coord, limit_coord, direction)
            q.append(matrix[coord[0]][coord[1]])
        
        coord = (n, matrix_len - 1 - n)
        direction = 1
        for i in range(steps):
            coord, direction = self.next_coord(coord, limit_coord, direction)
            matrix[coord[0]][coord[1]] = q.pop(0)

    def next_direction(self, direction):
        if direction == 3: 
            return 0
        else:
            return direction + 1

    def next_coord(self, coord, limit_coord, direction):
        (x, y) = coord
        (min_x, max_x, min_y, max_y) = limit_coord
        
        if min_x == max_x or min_y == max_y:
            return (x, y), direction
        
        if (y == max_y and direction == 0) or (x == max_x and direction == 1) or (y == min_y and direction == 2) or (x == min_x and direction == 3):
            direction = self.next_direction(direction)
        
        new_coord = None
        if direction == 0:
            new_coord = (x, y + 1)
        elif direction == 1:
            new_coord = (x + 1, y)
        elif direction == 2:
            new_coord = (x, y - 1)
        else:
            new_coord = (x - 1, y)
        
        return new_coord, direction