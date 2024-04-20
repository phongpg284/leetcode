class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    self.helper(land, i, j, [i, j], res)
        return res

    def helper(self, land, x, y, start, res):
        m, n = len(land), len(land[0])
        directions = [(0, 1), (1, 0)]

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_x < m and 0 <= new_y < n and land[new_x][new_y] == 1:
                land[new_x][new_y] = -1
                self.helper(land, new_x, new_y, start, res)

        if (x + 1 >= m or land[x + 1][y] == 0) and (y + 1 >= n or land[x][y + 1] == 0):
            res.append(start + [x, y])
