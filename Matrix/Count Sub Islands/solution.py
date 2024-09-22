class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        flag = [False]
        res = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    flag[0] = True
                    self.dfs(i, j, m, n, flag, grid1, grid2)

                    if flag[0]:
                        res += 1

        return res

    def dfs(self, i, j, m, n, flag, grid1, grid2):
        if i < 0 or j < 0 or i >= m or j >= n or grid2[i][j] == 0:
            return

        if grid1[i][j] != 1:
            flag[0] = False

        grid2[i][j] = 0

        self.dfs(i + 1, j, m, n, flag, grid1, grid2)
        self.dfs(i - 1, j, m, n, flag, grid1, grid2)
        self.dfs(i, j + 1, m, n, flag, grid1, grid2)
        self.dfs(i, j - 1, m, n, flag, grid1, grid2)
