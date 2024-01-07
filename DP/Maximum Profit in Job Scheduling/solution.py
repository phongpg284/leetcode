class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        jobs = sorted(zip(endTime, startTime, profit))

        dp = [0] * (n + 1)
        for i in range(n):
            end, start, cur_profit = jobs[i]
            index = bisect_right(jobs, start, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[index] + cur_profit)

        return dp[n]
