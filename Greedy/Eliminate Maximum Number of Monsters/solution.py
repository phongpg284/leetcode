class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        time = [dist[i] / speed[i] for i in range(n)]
        time = sorted(time)
        for i in range(n):
            if i >= time[i]:
                return i
        return n