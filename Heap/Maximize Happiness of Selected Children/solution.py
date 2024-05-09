class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res = 0
        happiness = [-happy for happy in happiness]
        heapq.heapify(happiness)

        for i in range(k):
            top = heapq.heappop(happiness)
            if top + i >= 0:
                return res
            res -= top + i
        return res
