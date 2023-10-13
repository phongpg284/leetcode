class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev, cur = cost[0], cost[1]
        for i in range(2, n):
            res = min(prev, cur) + cost[i]
            prev = cur
            cur = res
        return min(prev, cur)