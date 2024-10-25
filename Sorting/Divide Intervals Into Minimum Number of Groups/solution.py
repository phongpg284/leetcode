class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_time = sorted(interval[0] for interval in intervals)
        end_time = sorted(interval[1] for interval in intervals)

        i, res = 0, 0

        for start in start_time:
            if start > end_time[i]:
                i += 1
            else:
                res += 1

        return res
