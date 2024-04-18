class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                res += self.get_perimeter(grid, i, j)
        return res

    def get_perimeter(self, grid, x, y):
        if grid[x][y] == 0:
            return 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        side = 0

        for i, j in directions:
            new_x = x + i
            new_y = y + j

            if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                side += 1
            else:
                if grid[new_x][new_y] == 0:
                    side += 1
        return side
