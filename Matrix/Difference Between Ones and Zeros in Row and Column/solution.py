class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        row_one = [0] * m
        col_one = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_one[i] += 1
                    col_one[j] += 1
        
        res = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                res[i][j] = row_one[i] + col_one[j] - (n - row_one[i]) - (m - col_one[j])
        return res