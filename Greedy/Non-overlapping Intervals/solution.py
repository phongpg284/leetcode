class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        n = len(intervals)
        count = 0
        prev = 0

        for i in range(n):
            if i == 0:
                count += 1
            else:
                if intervals[i][0] >= intervals[prev][1]:
                    prev = i
                    count += 1
        return n - count
