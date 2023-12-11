class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        flags = [1] * n
        for i in range(n - 1):
            for j in range(i + 1, n):
                if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
                    flags[j] = 0
                elif intervals[j][0] <= intervals[i][0] and intervals[j][1] >= intervals[i][1]:
                    flags[i] = 0
                    break
        return sum(flags)