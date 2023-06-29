from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])
        keys = 0
        start = (0, 0)
        steps = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    start = (i, j)
                if grid[i][j].islower():
                    keys += 1
        
        stack = deque([(start[0], start[1], 0)])
        visited = set()
        visited.add((start[0], start[1], 0))
        
        while stack:
            for _ in range(len(stack)):
                i, j, key = stack.popleft()
                if grid[i][j].islower():
                    key |= 1 << (ord(grid[i][j]) - ord('a'))
                if key == (1 << keys) - 1:
                    return steps
                for r, c in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] != '#':
                        if grid[r][c].isupper() and key & (1 << (ord(grid[r][c]) - ord('A'))) == 0:
                            continue
                        if (r, c, key) not in visited:
                            stack.append((r, c, key))
                            visited.add((r, c, key))
            steps += 1
        return -1
