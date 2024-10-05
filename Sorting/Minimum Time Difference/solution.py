class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        format_time = []
        for time in timePoints:
            times = time.split(':')
            hour = int(times[0])
            minute = int(times[1])
            format_time.append(hour * 60 + minute)

        format_time = sorted(format_time)

        res = format_time[0] + 24 * 60 - format_time[-1]
        for i in range(len(format_time) - 1):
            res = min(res, format_time[i + 1] - format_time[i])

        return res
