class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        point = [[float('inf')] * n for _ in range(n)]
        self.bfs(grid, point)

        visited = [[False] * n for _ in range(n)]
        heap = [(-point[0][0], 0, 0)]

        while heap:
            p, x, y = heapq.heappop(heap)
            p = -p

            if x == n - 1 and y == n - 1:
                return p

            visited[x][y] = True

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y]:
                    new_p = min(p, point[new_x][new_y])
                    heapq.heappush(heap, (-new_p, new_x, new_y))
                    visited[new_x][new_y] = True
        return -1

    def bfs(self, grid, point):
        n = len(grid)
        q = deque()
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    point[i][j] = 0
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            p = point[x][y]

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if 0 <= new_x < n and 0 <= new_y < n and point[new_x][new_y] > p + 1:
                    point[new_x][new_y] = p + 1
                    q.append((new_x, new_y))
