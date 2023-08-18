class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        directs = [0] * n
        res = 0
        for road in roads:
            directs[road[0]] += 1
            directs[road[1]] += 1
        roads_set = set(tuple(road) for road in roads)
        for i in range(n - 1):
            for j in range(i + 1, n):
                temp = directs[i] + directs[j]
                if (i, j) in roads_set or (j, i) in roads_set:
                    temp -=1
                res = max(res, temp)
        return res