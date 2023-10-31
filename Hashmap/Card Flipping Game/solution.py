class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        res = set()

        for i in range(n):
            res.add(fronts[i])
            res.add(backs[i])

        for i in range(n):
            if fronts[i] == backs[i]:
                res.discard(fronts[i])
        
        return min(res) if res else 0 