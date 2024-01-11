class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return sum([cost[0] for cost in costs]) + sum(sorted([cost[1] - cost[0] for cost in costs])[:len(costs)//2])