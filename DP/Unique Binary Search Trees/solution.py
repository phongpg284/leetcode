class Solution:
    def numTrees(self, n: int) -> int:
        map = [[0] * (n+1) for i in range(n+1)]
        map[0] = [1, 0]
        for i in range(1, n + 1):
            for j in range(0, i + 1):
                if j == 0 or j == i + 1:
                    map[i][j] = 0
                else:
                    sum = 0
                    for k in range(j-1, i + 1):
                        sum += map[i-1][k]
                    map[i][j] = sum

        sum = 0
        for i in range(1, n + 1):
            sum += map[n][i]
        return sum
