class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, i, j):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque([(i, j)])
        grid[i][j] = '0'

        while q:
            x, y = q.pop()

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]) and grid[new_x][new_y] == '1':
                    q.append((new_x, new_y))
                    grid[new_x][new_y] = '0'
