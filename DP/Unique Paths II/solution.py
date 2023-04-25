class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        map = [[0] * (n + 1) for i in range(m+1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i-1][j-1] == 0:
                    if (i == 1 and j == 1):
                        map[i][j] = 1
                    else:
                        map[i][j] = map[i - 1][j] + map[i][j - 1]
        return map[m][n]