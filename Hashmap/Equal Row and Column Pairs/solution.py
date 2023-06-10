class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        map = dict()
        res = 0
        for row in grid:
            if tuple(row) in map:
                map[tuple(row)] += 1
            else:
                map[tuple(row)] = 1
        n = len(grid)
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(grid[j][i])
            if tuple(temp) in map:
                res += map[tuple(temp)]
        return res
