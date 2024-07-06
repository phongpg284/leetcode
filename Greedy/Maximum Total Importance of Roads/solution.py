class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        neighbors_count = [0] * n

        for u, v in roads:
            neighbors_count[u] += 1
            neighbors_count[v] += 1

        neighbors_count = sorted(neighbors_count)

        res = 0

        for i in range(n):
            res += (i + 1) * neighbors_count[i]

        return res
